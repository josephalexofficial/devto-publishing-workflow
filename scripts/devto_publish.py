import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "articles"
DEVTO_API_URL = "https://dev.to/api/articles"


def parse_front_matter(text):
    if not text.startswith("---\n"):
        raise ValueError("Article must start with YAML-style front matter.")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("Article front matter must be closed with ---.")

    raw_front_matter = text[4:end]
    body = text[end + 5 :].lstrip()
    data = {}

    for line in raw_front_matter.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if ":" not in line:
            raise ValueError(f"Invalid front matter line: {line}")

        key, value = line.split(":", 1)
        data[key.strip()] = parse_value(value.strip())

    return data, body


def parse_value(value):
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() in {"null", "none"}:
        return None
    if value.startswith("[") and value.endswith("]"):
        return [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def render_front_matter(data, body):
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, bool):
            rendered = "true" if value else "false"
        elif isinstance(value, list):
            rendered = ", ".join(str(item) for item in value)
        elif value is None:
            rendered = ""
        else:
            rendered = str(value)
        lines.append(f"{key}: {rendered}")
    lines.append("---")
    lines.append("")
    lines.append(body.rstrip())
    lines.append("")
    return "\n".join(lines)


def article_payload(front_matter, body):
    required = ["title", "description", "tags"]
    missing = [field for field in required if not front_matter.get(field)]
    if missing:
        raise ValueError(f"Missing required front matter fields: {', '.join(missing)}")

    tags = front_matter["tags"]
    if isinstance(tags, str):
        tags = [tag.strip() for tag in tags.split(",") if tag.strip()]

    article = {
        "title": front_matter["title"],
        "body_markdown": body,
        "published": bool(front_matter.get("published", False)),
        "description": front_matter["description"],
        "tags": tags[:4],
    }

    optional_fields = {
        "canonical_url": "canonical_url",
        "series": "series",
        "cover_image": "main_image",
        "organization_id": "organization_id",
    }

    for source_key, api_key in optional_fields.items():
        value = front_matter.get(source_key)
        if value:
            article[api_key] = value

    return {"article": article}


def request_devto(method, api_key, payload, article_id=None):
    url = DEVTO_API_URL if article_id is None else f"{DEVTO_API_URL}/{article_id}"
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        details = error.read().decode("utf-8")
        raise RuntimeError(f"DEV.to API error {error.code}: {details}") from error


def publish_article(path, api_key):
    text = path.read_text(encoding="utf-8")
    front_matter, body = parse_front_matter(text)
    payload = article_payload(front_matter, body)
    devto_id = front_matter.get("devto_id")

    if devto_id:
        result = request_devto("PUT", api_key, payload, article_id=devto_id)
        print(f"Updated DEV.to article {devto_id}: {path}")
        return False, result

    result = request_devto("POST", api_key, payload)
    new_id = result.get("id")
    if not new_id:
        raise RuntimeError(f"DEV.to did not return an article id for {path}")

    front_matter["devto_id"] = new_id
    path.write_text(render_front_matter(front_matter, body), encoding="utf-8")
    print(f"Created DEV.to article {new_id}: {path}")
    return True, result


def main():
    api_key = os.environ.get("DEVTO_API_KEY")
    if not api_key:
        print("Missing DEVTO_API_KEY environment variable.", file=sys.stderr)
        return 1

    if not ARTICLES_DIR.exists():
        print("No articles directory found. Nothing to publish.")
        return 0

    article_paths = sorted(
        path
        for path in ARTICLES_DIR.rglob("*.md")
        if not re.search(r"(^|[\\/])_", str(path.relative_to(ARTICLES_DIR)))
    )

    if not article_paths:
        print("No Markdown articles found.")
        return 0

    created_any = False
    for path in article_paths:
        created, _ = publish_article(path, api_key)
        created_any = created_any or created

    if created_any:
        print("One or more new DEV.to article ids were written back to Markdown files.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
