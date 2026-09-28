---
title: Keep the Last Look: A Practical Guide to Reviewing AI-Assisted Work
published: true
description: A practical guide to reviewing AI-assisted work so the final result matches the goal, the evidence, and the risks you are willing to accept.
tags: ai, beginners, productivity, career
---

## Introduction

An AI agent can draft the email, edit the code, summarize the notes, or prepare the article. It can also sound finished before the work is finished.

That is the moment that matters. The agent has returned something plausible, often something useful, and the easiest next step is to accept it. The better next step is a last look: a short, deliberate review that asks whether the result matches the goal you actually had.

This is not a call to distrust every suggestion. It is a way to keep the benefit of speed without giving away the judgment that makes the work yours. A last look is how AI-assisted work becomes reliable work.

## Why the Last Look Exists

AI tools are good at producing a complete-looking surface. Sentences connect. Code compiles. A plan has headings. The shape of a finished thing arrives before you have checked the substance.

The gaps tend to hide in ordinary places:

- A requirement was misunderstood.
- A fact was stated with confidence and no source.
- A change fixed the example and missed the real case.
- A file was edited, but the surrounding system was left inconsistent.
- The tone fits a generic reader, not the person you are writing for.

None of these failures announce themselves. They sit inside work that looks ready. The last look is the habit of finding them while the change is still small.

## Review the Outcome Before the Details

Start with the original request, not with the first paragraph or the first changed line.

Read the goal again, in the words you used. Then look at the result and answer one question: if this were accepted exactly as it is, would the goal be met?

That question saves time. A beautiful explanation of the wrong problem does not need line-by-line editing. A code change that solves a different bug does not need a style pass. Send it back, or revise the goal, before you polish the surface.

Write the outcome in a sentence you can test:

> The article is public, the same post is updated on later edits, and a reader can follow the steps without guessing.

Now the review has a target. You are no longer asking "does this look good?" You are asking "does this do the thing?"

## Use Five Layers

A reliable review moves from the outside inward. Each layer answers a different question, and you stop early if an outer layer fails.

| Layer | Question | What you look for |
| --- | --- | --- |
| Outcome | Did this meet the goal? | The requested result, not a nearby one |
| Evidence | What proves it? | A test, a source, a preview, or a page you opened |
| Changes | What actually moved? | Files, claims, numbers, and steps that differ from before |
| Risks | What could still go wrong? | Secrets, broken neighbors, overstated certainty |
| Leftovers | What remains unfinished? | TODOs, unused pieces, and questions the tool skipped |

This order matters. Evidence is meaningless if the outcome is wrong. A risk review is wasted on a change you are about to reject. Leftovers are the last pass, when you already believe the main result is sound.

## Ask for Evidence You Can See

Fluency is not evidence. An agent can describe a successful test, a cited paper, or a published page without those things existing in the form you need.

Match the claim to a check you can perform:

- If it says the tests pass, run the tests.
- If it says the page is live, open the page.
- If it quotes a number, find the number.
- If it says a file was updated, open the file.
- If it recommends a tool or an API, confirm the name and the current behavior.

You do not need to re-do the entire task. You need to sample the claims that carry the conclusion. The more important the claim, the less you should accept it as narration.

A useful sentence to keep nearby is: "Show me the thing that proves this." Good agents can point to a file, a log, a command, or a link. If they can only repeat the conclusion in different words, the review is not finished.

## Read the Change, Not Only the Summary

A summary is a guide. The change is the work.

When an agent says "I added validation," look at the validation. When it says "I clarified the introduction," read the introduction beside the goal. Summaries compress. Compression drops the edge cases, the names, and the quiet assumptions.

For writing, read the piece once as a reader who does not know the conversation that produced it. Mark any sentence that requires a private context the public reader will not have. Those sentences felt clear in the chat. They are not clear on the page.

For code, read the diff with three questions:

1. What behavior changed for the person using this?
2. What nearby behavior should have stayed the same?
3. Is there a path that the change does not cover?

The third question is where rushed AI edits usually fail. The happy path is present. The empty state, the second run, the missing credential, or the already-existing record was never in the example the agent saw.

## Watch for Confident Gaps

Some problems are obvious: the code does not run, the link is broken, the heading is missing. The harder problems are the confident gaps. The work sounds sure, and the surety is doing the job that evidence should have done.

Pause when you see these patterns:

- Exact numbers with no source.
- "Always" and "never" wrapped around a complicated topic.
- A new dependency, credential, or permission that was not requested.
- A rewrite of working parts that were outside the task.
- A conclusion that skips the case where the first attempt fails.

None of these is automatically wrong. Each one is a place to slow down. Ask where the certainty came from. If the answer is "the draft sounded finished," it is not yet evidence.

## A Worked Review

Imagine you asked an agent to publish an article from a Markdown file. It replies that the workflow succeeded and the post is live.

A last look does not start by admiring the workflow file. It starts with the outcome.

1. Open the public profile and find the article.
2. Confirm it is public, not sitting in drafts.
3. Compare the title, the opening, and a middle section with the source file.
4. Check that a second run would update this article, because an id was saved, rather than create another one.
5. Read the job result and confirm the success refers to this article, not to an earlier run.

Only after those checks is the summary trustworthy. "The workflow passed" might mean an old run passed. "The article exists" might mean a draft exists. The last look ties the claim to the thing you can see.

The same pattern works for a bug fix. Reproduce the original failure, or confirm why you no longer can. Then try the neighboring case the bug might have disturbed. A fix that only satisfies the reported example is a partial fix, even when the write-up is excellent.

## Keep a Review That Fits the Risk

Not every task deserves the same depth. A thrown-away experiment can survive a light read. A public article, a payment change, a migration, or a message to a customer deserves a slower pass.

Choose the depth on purpose:

- **Light:** read the outcome and skim the result. Use this for disposable drafts.
- **Standard:** check the outcome, one piece of evidence, and the diff. Use this for normal daily work.
- **Close:** check every layer, including risks and leftovers. Use this when the result will be public, hard to undo, or trusted by someone else.

The point of the scale is consistency. If everything receives a close review, the habit collapses under its own weight. If nothing does, speed becomes a way of shipping unseen mistakes. Match the look to the cost of being wrong.

## Make the Next Review Easier

A last look should leave the work easier to review the next time, not harder.

You can do that in small ways:

- Keep the original goal written down.
- Save ids, links, and commands that proved the result.
- Separate what changed from what you decided not to change.
- Remove unused alternatives so the next reader sees one path.
- Note a risk you accepted, so it is a decision and not an accident.

This is also how you work better with agents over time. The next prompt can include the checks you care about: "Update the existing article, then give me the public link," or "Show the test you ran and the case you did not run." A clear review standard becomes a clearer request.

## A Checklist You Can Reuse

Before you accept AI-assisted work, walk through this list.

- I can restate the goal in one sentence.
- The result meets that goal, not a nearby one.
- I checked at least one claim against something I can see.
- I looked at the actual change, not only the summary.
- I know what should have stayed the same.
- I looked for secrets, extra permissions, and unsupported certainty.
- I know what is still unfinished.
- The depth of this review matches the cost of a mistake.
- A later run or a later reader can find the proof.

If you cannot tick the first three, the work is not ready. The rest of the list is how you finish with confidence.

## Final Thoughts

AI agents can make the first draft, the first patch, and the first plan arrive quickly. The value of the work still depends on the last look.

Keep that look small enough to practice and serious enough to matter. Return to the goal. Ask for evidence you can open. Read the change itself. Notice where confidence is standing in for proof. Then accept the work because you checked it, not only because it arrived looking complete.

Speed is a gift. Judgment is still the job.
