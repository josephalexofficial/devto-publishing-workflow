# devto-publishing-workflow

A GitHub-powered workflow for drafting, versioning, and publishing Markdown articles to DEV.to.

## Overview

This repository keeps articles in Markdown, stores their history in GitHub, and uses GitHub Actions to publish them to DEV.to.

It is designed to be reusable. One workflow can handle the first article and every future article added to the `articles/` folder.

## Repository Structure

```text
.
├── articles/
│   └── ai-agents-not-magic.md
├── scripts/
│   └── devto_publish.py
└── .github/
    └── workflows/
        └── publish-devto.yml
```

## How Publishing Works

When changes are pushed to the `main` branch, GitHub Actions runs the publisher script.

The script checks every Markdown file in `articles/`:

- Articles without a `devto_id` are created on DEV.to.
- Articles with a `devto_id` update the existing DEV.to post.
- Articles with `published: false` remain drafts.
- Articles with `published: true` are published publicly.

After a new article is created, the workflow saves its DEV.to article id back into the Markdown file. That makes future updates reliable because the workflow knows which DEV.to post belongs to each file.

## First-Time Setup

Before publishing can work, add your DEV.to API key to the GitHub repository:

1. Open DEV.to.
2. Go to `Settings`.
3. Open `Extensions`.
4. Generate a DEV.to API key.
5. Open this GitHub repository.
6. Go to `Settings` > `Secrets and variables` > `Actions`.
7. Create a repository secret named `DEVTO_API_KEY`.
8. Paste your DEV.to API key as the secret value.

If the secret is missing, the workflow skips publishing instead of failing.

## Article Format

Each article must start with front matter:

```md
---
title: Example Article Title
published: false
description: A short description of the article.
tags: ai, beginners, webdev, productivity
---
```

Keep `published: false` while drafting. Change it to `published: true` only when the article is ready to go live.

## Adding Future Articles

For a future article, create a new file such as:

```text
articles/my-next-article.md
```

Use the same front matter format, write the article, and push it to GitHub. The existing workflow will handle the rest.

## Current Article

The first article in this repository is:

`AI Agents Are Not Magic: A Beginner's Guide to How They Think, Use Tools, and Get Things Done`
