<!-- Chapter 5: The Email Machine. Rules file from Appendix B, Email Rules File Template. -->
# Chapter 5: Morning email triage

Start here if you only set up one thing from the book. It's the one you'll keep.

## Your rules file

Drag [`email-rules.txt`](email-rules.txt) onto your Desktop (on GitHub: open it, then the download button, or Raw and File > Save As). Open it in TextEdit and fill every bracket:

- `[name 1]`, `[name 2]`, `[name 3]`: the people whose email is always urgent. Real names. "Any email from Sarah" works; "important people" doesn't, because Claude can't know who you mean. Add more names if you have them.
- `[your bank]`, `[your doctor/healthcare provider]`, `[HR department]`: senders Claude should never open (chapter 11 explains why).
- The two newsletter lines: the ones you read go under FYI, the ones you don't go under ARCHIVE.
- `[specific sources]`: the industry news you actually follow, or delete the line.

Change the urgency keywords if "deadline" and "ASAP" aren't yours. Delete the `#` line at the top. Keep the name `email-rules.txt` and keep it on the Desktop. The prompt looks for it there.

## Paste the triage prompt

Sign in to your email in the browser first. Then paste this into the Cowork chat:

```
Read the file email-rules.txt on my Desktop. Then open Safari and go to mail.google.com (or open Mail/Outlook if you use those). Read all unread emails in my inbox. For each email, categorize it using the rules in email-rules.txt. For emails in the "Needs My Reply" category, draft a reply based on the email thread context. Save a summary document to my Desktop called "inbox-summary-[today's date].txt" with the following sections: URGENT (with sender, subject, and why it is urgent), NEEDS MY REPLY (with sender, subject, and the draft reply I should review), FYI (sender and subject only), and ARCHIVE (count only, do not list individual emails). Do not archive anything on this first run. Instead, for every email you put in the ARCHIVE category, apply the Gmail label "Claude-Archive-Review" (in a mail client without labels, list those emails by sender and subject at the bottom of the summary under "ARCHIVE CANDIDATES"). I will review them and tell you when to start archiving automatically.
```

On Apple Mail, add this sentence to the end so Claude reads whole threads:

```
Expand all conversation threads before reading.
```

Stay nearby for the first 20 or 30 emails. Every call you disagree with is a line to fix in `email-rules.txt`.

## What you should have

- `inbox-summary-` plus today's date, as a `.txt` file on your Desktop, with URGENT, NEEDS MY REPLY (each with a draft reply), FYI, and an ARCHIVE count.
- In Gmail, a label called `Claude-Archive-Review` holding the archive candidates. In a client without labels, an ARCHIVE CANDIDATES list at the bottom of the summary.
- Nothing archived or sent. If either happened, stop and check the prompt.

## Before you let it archive

Open `Claude-Archive-Review` each morning and look for anything that shouldn't be there. After a week or two of runs where it's always right, change the prompt's archive sentences to "archive all emails in the ARCHIVE category". Keep "Ask before acting" on so you still see the batch before it moves.

If the drafts sound stiff after the first week, edit the DRAFT REPLY GUIDELINES lines in `email-rules.txt`. The tone rule is already there.

## Sending the replies

Don't let Claude send email without your approval in the first two weeks. One wrong auto-sent email costs more than the time saved.

- **Gmail connector:** Claude can write drafts into Gmail but can't send. You open each draft and press Send.
- **Computer Use in the browser:** Claude can send, one at a time, after you approve each one:

```
Open Gmail. For each draft reply in the inbox summary, find the email thread and send the reply. Ask me for approval before each send.
```

## Find dropped threads

Run this at the end of the day or on Friday afternoon:

```
Open my email client. Find any threads where I sent a message more than 3 days ago and have not received a reply. List them in a document called "follow-ups-needed.txt" on my Desktop with the recipient, subject, date I sent my last message, and how many days since my message.
```

## Job applications, supervised

Read this before you run it. LinkedIn and Indeed can limit or lock accounts that apply faster than a person could, and their terms don't allow automated applying. Click Submit yourself every time. Solve CAPTCHAs yourself. Don't send fifty in one sitting. Start with 20.

Put your resume on the Desktop as a PDF or Word file, then fill `[job board URL]`, `[your job title]`, `[your city or "remote"]` and `[path to resume file on your Desktop]`:

```
Open Safari and go to [job board URL]. Search for [your job title] in [your city or "remote"]. For each job listing in the results: open the listing, read the job description, check if my resume matches at least 70% of the requirements (my resume is saved at [path to resume file on your Desktop]). If it matches, fill in the application, and if there is a cover letter field, write a cover letter that references 2-3 specific requirements from the job description and explains how my experience matches. Then STOP and show me the completed application so I can review it and click Submit myself. After I approve and submit, move to the next listing. Stop after 20 applications or when you reach the end of the search results, whichever comes first.
```

To keep a record, send this first:

```
Create a spreadsheet on my Desktop called job-applications.csv with columns for Company, Position, Date Applied, Job Board, and Status.
```

and add this to the end of the application prompt:

```
After each application, add a row to job-applications.csv with the company name, position title, today's date, the job board name, and 'Applied' as the status.
```

## Make it daily

The triage prompt is already in [`cowork-templates.txt`](../../cowork-templates.txt). To have it run at 6:00am on weekdays, paste it into `/schedule`: [chapter 8](../08-scheduled-tasks/README.md).
