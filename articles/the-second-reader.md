---
title: The Second Reader: A Practical Guide to Writing That Still Makes Sense Later
published: true
description: A practical guide to writing technical work for the person who arrives later, without the meeting, the chat, or the private context.
tags: beginners, productivity, career, tutorial
devto_id: 4773673
---

## Introduction

The first reader of a piece of technical work is usually close to it. They were in the meeting. They saw the error. They watched the draft change. A sentence that says "use the same approach as yesterday" is clear to them, because yesterday is still in the room.

The second reader arrives later. They have the page, the file, or the repository, and none of the conversation that produced it. If the writing only works for the first reader, the work expires the moment the chat closes.

This article is a practical way to write for that second reader. It applies to articles, README files, pull request notes, setup guides, and the explanation you leave beside a workflow. The standard is simple: a careful person should be able to understand the work without asking you what you meant.

## Who the Second Reader Is

The second reader is not a beginner by default, and not an expert by default. They are a person with enough skill to follow a clear explanation, and no access to your private context.

They might be:

- You, six weeks from now, returning to a project you thought you would remember.
- A teammate opening a repository for the first time.
- A reader on a public profile who found the article through a title and a tag.
- A reviewer deciding whether a change is safe.
- An agent, or another tool, following written instructions on a later run.

These people share one limitation. They cannot hear the tone you would use if you were standing next to them. The page has to carry that guidance.

Write as if the second reader is capable and new to this specific work. Capable means you do not explain what a folder is. New to this work means you do explain which folder matters here, and why.

## What Disappears When the Conversation Ends

A lot of meaning hides in things that never get written down.

| Private context | What the second reader has instead |
| --- | --- |
| The meeting where the goal was agreed | The goal, if you wrote it down |
| The error you already saw | The symptom, if you recorded it |
| The option you rejected | The decision, if you named it |
| The nickname your team uses | The real name of the file, command, or page |
| "You know what I mean" | Only the words on the page |

If a sentence depends on a row in the left column, it will fail for the second reader. Move the necessary meaning into the right column. Leave the rest out.

A useful test is to read the piece in a new window, with the chat and the notes closed. Anywhere you feel the urge to say "well, what I meant was," the sentence needs to be rewritten now, while you still remember.

## Lead With Where the Reader Will Arrive

Open with the destination. The second reader should know, within the first few lines, what they will be able to do or understand when they finish.

Weak openings start with the author's timeline: how long the problem took, which tools were considered, and how confusing it felt. Those details can belong later. They do not belong first, because the reader cannot yet tell whether the page is for them.

A strong opening answers three questions:

1. What is this about, in concrete terms?
2. Who is it for?
3. What will be true for the reader at the end?

Here is a destination written as a sentence you can test:

> After reading this, you can add a Markdown article to the repository and know whether the workflow will create a new post or update an existing one.

That sentence gives the second reader a reason to continue. It also gives you a standard for the rest of the piece. If a section does not serve that destination, it is optional. If the piece never reaches that destination, it is not finished.

## Replace Nicknames With Landmarks

Teams compress language. A file becomes "the script." A page becomes "the dashboard." A branch becomes "the usual one." Compression is comfortable in a conversation. On a page, it makes the reader search.

Use landmarks the second reader can find without you:

- The file name, not "the main file."
- The command, not "the normal command."
- The page name, not "settings, you know the one."
- The exact label of a button or secret, not a description of where you remember it being.

Quote the names as they appear. If a secret must be named `DEVTO_API_KEY`, write `DEVTO_API_KEY`. If the articles live in `articles/`, write `articles/`. A landmark is kind because it removes a search.

When a landmark may move, say what it is for as well as what it is called. "The repository secret named `DEVTO_API_KEY` stores the key the workflow uses to publish." The name can change later. The purpose still tells the next reader what to look for.

## Show the Path, Then the Reason

The second reader often needs two layers: what to do, and why this path is the one you chose. Give them in that order. A reason before a path makes the reader hold an abstraction they cannot use yet. A path without a reason makes the next exception impossible to judge.

A clean section follows this shape:

1. Say what the reader is about to do.
2. Show the step in the order they will meet it.
3. Add the reason that prevents a likely mistake.
4. Say how they can tell the step worked.

For example:

> Add `published: true` at the top of the article when it should appear on your public profile. Leave it `false` while you still want a draft. After the workflow runs, open your profile and confirm the post is public. A successful job only proves that the program finished. The profile proves that the article is visible.

The reason is attached to a step the reader can perform. It is not a general essay about publishing. The check is something they can see.

## Name the Decision, Not Only the Result

Finished work hides the choices that made it. The second reader meets the result and has to guess which parts are deliberate.

Name the decisions that a later person might be tempted to undo:

- We update an existing post when an id is already saved, so a second run does not create a duplicate.
- The workflow reads Markdown from the repository, so the file remains the source of truth.
- A missing credential stops the run with a clear message, so a forgotten secret does not look like a successful publish.

You do not need a history of every alternative. You need the decision, the reason, and the consequence of reversing it. One short paragraph can save a later reader from "improving" the work back into a problem you already solved.

If you rejected an approach, say so only when the rejection protects the reader. "We did not create a separate workflow for each article, because one workflow already handles every file in the folder." That sentence prevents a reasonable mistake. A diary of unused ideas does not.

## Write the Exception Beside the Rule

Most instructions describe the happy path. The second reader usually arrives because the happy path did not happen. Put the exception near the rule it belongs to, not in a troubleshooting section they may never reach.

| Rule | Exception to mention beside it |
| --- | --- |
| A new file creates a new post | A file that already has an id updates the existing post |
| A green check means the job finished | The public page is the proof that the post is visible |
| Drafts stay unpublished | `published: true` is what makes the post public |
| One workflow handles every article | A new article is a new file, not a new workflow |

This is also a kindness to your future self. When a run fails, the page you wrote should already contain the distinction you will wish you remembered.

Keep each exception specific. "Sometimes this fails" is not guidance. "If the title was created in the last few minutes, find the existing post and save its id" is guidance.

## Cut Sentences That Only You Can Finish

Read each paragraph and mark any sentence that needs your voice to complete it. These are common forms:

- "As we discussed..."
- "Simply use the usual process."
- "This is obvious once you see it."
- "Just click the right setting."
- "We fixed the issue from before."

Replace them with the missing noun. "As we discussed" becomes the decision. "The usual process" becomes the steps. "The issue from before" becomes the symptom and the repair.

Then read the piece aloud once. Your ear will catch a jump that your eyes treat as familiar. If you have to breathe in extra explanation between two sentences, that explanation belongs on the page.

## A Short Pattern You Can Reuse

When you finish a piece of work and need to leave it understandable, draft the handoff in this order:

```text
Destination: what the reader can do when they finish
Landmarks: the exact names they must find
Path: the steps, in the order they happen
Check: what they can see if it worked
Decision: what they should not casually reverse
Exception: the nearby case that looks similar but is different
```

You can write this as six sentences before you write the full article, the README section, or the pull request. If one of the six is difficult, that is the part the second reader would have had to ask you about. Write that part first.

The pattern is short enough to use on a small change and sturdy enough to hold a long guide. Length is not the goal. A complete handoff can be a page. An incomplete one can be ten pages and still force the reader to guess.

## A Checklist Before You Publish

Before you call a piece ready for someone who was not in the room, confirm this list.

- The opening says what the reader will be able to do or understand.
- Important names match the real files, commands, buttons, and secrets.
- Steps appear in the order the reader will meet them.
- Each important step says how to tell that it worked.
- A decision the reader might undo is named, with its reason.
- The likely exception sits beside the rule it affects.
- No sentence depends on a meeting, a chat, or a memory.
- You can follow the piece with the surrounding conversation closed.

If the last item fails, the piece is still a note to yourself. That can be useful. It is not yet writing for the second reader.

## Final Thoughts

The first reader is easy to serve, because they already know the story. The second reader is the one who tells you whether the work can travel.

Write the destination first. Use names a stranger can find. Show the path, the check, the decision, and the nearby exception. Then close the chat and read it as if you were arriving late.

When the page still makes sense, you have written for the second reader. That is the version worth publishing, because it keeps working after the conversation ends.
