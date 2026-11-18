<!-- Chapter 11: What Can Go Wrong (And How to Stay Safe) -->
# Chapter 11: The three rules

Never auto-send to anyone outside. Keep sensitive files and senders out of Claude's reach. Review every new workflow for two weeks before you trust it.

**The Safe Mode prefix.** Paste this in front of any workflow you haven't run before. It's also in [`cowork-templates.txt`](../../cowork-templates.txt).

```
SAFETY RULES FOR THIS TASK: 1) Do not send, submit, or post anything to any external recipient. Save all drafts and outputs as files on my Desktop for my review. 2) Skip any folder named "No-AI" or "Private." Do not open, read, or list files in those folders. Skip emails from senders listed in the SKIP section of email-rules.txt. 3) Before performing any action that deletes, moves, or modifies existing files, or before clicking Send/Submit on any form, state what you are about to do in the chat and wait for my approval. Now proceed with the following task:
```

After two weeks of clean runs you can drop rule 3 for that one workflow. Rule 1 stays on.

## Keep a No-AI folder

Make a folder called `No-AI` outside every connected folder (chapter 11 has the steps), then check that Claude leaves it alone:

```
List every folder on my Desktop. For each folder, list the files inside it. If you encounter a folder called "No-AI" or "Private," do NOT list its contents. Instead, write "SKIPPED - restricted folder" and move on. Save the results as "access-test.txt" on my Desktop.
```

Open `access-test.txt`. It worked if the No-AI folder reads "SKIPPED - restricted folder" and the other folders are listed normally. Add this line to every prompt that touches your files:

```
Skip any folder named 'No-AI' or 'Private.' Do not open, read, or list files in those folders.
```

Your `email-rules.txt` from chapter 5 already starts with a SKIP section. The book's own example of a filled-in one:

```
SKIP (do not read or process):
- Any email from Chase Bank
- Any email from Kaiser Permanente
- Any email from [your company] HR Department
- Any email with subject containing "password reset" or "SSN"
```

## Words that move files

Vague verbs like "clean up" can end in the Trash. Say exactly where files go:

```
Move files older than 30 days to a folder called Archive
```

To keep the Desktop from filling up, add this to the end-of-day task:

```
Move any files on my Desktop older than 7 days into a folder called Desktop-Archive.
```
