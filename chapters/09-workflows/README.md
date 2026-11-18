<!-- Chapter 9: Building Complete Workflows (The Compound Effect) -->
# Chapter 9: One instruction, a whole chain

A workflow is one prompt with numbered steps that run in order in a single conversation, each step saving a file the next step reads. Pick one of the three below. If you invoice clients, start with Wednesday: it's the one that brings money in sooner.

## The data files

The invoice and report workflows read four CSVs. These have the book's columns and three fake rows each, so you can see the format. Replace the rows with your own, or export from your own tools with the same column names.

| File | Columns | Where it goes |
|---|---|---|
| [`invoices.csv`](invoices.csv) | Invoice Number, Client, Invoice Date, Amount, Status ("Sent" or "Paid") | an Accounting folder in Google Drive |
| [`bank-transactions.csv`](bank-transactions.csv) | Date, Description, Amount | Desktop |
| [`time-tracking.csv`](time-tracking.csv) | Date, Client, Hours, Notes | Google Drive |
| [`client-budgets.csv`](client-budgets.csv) | Client, Budget Hours, Hours Used | Google Drive |

## Build it a step at a time

Run Step 1 alone and open its file. Then Steps 1 and 2. Then the whole thing. When a full run comes out right, paste it into `/schedule` ([chapter 8](../08-scheduled-tasks/README.md)). If a later step comes out wrong, the earlier step's file tells you where it went off.

The bare pattern, for designing your own:

```
Complete the following steps in order. After each step, save intermediate results so I can review your progress if I check the conversation.

Step 1: [first task - produces output A]
Step 2: Using the results from Step 1, [second task - produces output B]
Step 3: Using the results from Steps 1 and 2, [third task - produces output C]
Step 4: Compile outputs A, B, and C into [final deliverable]
```

## Monday: meeting prep

Put your client names where it says `[list your active clients]`.

```
Complete the following workflow. Save intermediate results to files on my Desktop as you go.

STEP 1 - Calendar Review:
Read my calendar for this week (Monday through Friday). List every meeting with the attendee names, date, time, and subject. Save this as "weekly-calendar.txt" on my Desktop.

STEP 2 - Client File Check:
For each meeting that involves a client (any meeting where the subject or attendee name matches one of these client names: [list your active clients]), open my Google Drive and find that client's folder. Check the 3 most recently modified files in each client folder. Note the file names, last modified dates, and whether anything was modified in the past 7 days. Save this as "client-files-status.txt" on my Desktop.

STEP 3 - Email Check:
Read my inbox for any emails from the clients identified in Step 2, received in the past 7 days. For each email, note the sender, subject, date, and a 1-sentence summary. Save this as "client-emails.txt" on my Desktop.

STEP 4 - Weekly Prep Summary:
Compile the results from Steps 1-3 into a single document called "weekly-prep-[today's date].md" on my Desktop. Format it as:
- Section 1: This Week's Meetings (sorted by date/time)
- Section 2: Client Activity Summary (for each client: recent file changes, recent emails, any open items)
- Section 3: Action Items (anything that needs my attention before the meetings)
- Section 4: Prep Notes (suggested talking points for each client meeting based on their recent activity)

When all steps are complete, give me a brief summary in the chat.
```

## Wednesday: overdue invoices

```
Complete the following workflow. Save intermediate results as you go.

STEP 1 - Invoice Check:
Read the file "invoices.csv" in my Google Drive Accounting folder. Identify any invoices with a Status of "Sent" where the Invoice Date is more than 14 days ago. These are overdue. List them with the client name, invoice number, amount, and days overdue. Save as "overdue-invoices.txt" on my Desktop.

STEP 2 - Payment History Check:
For each overdue invoice, check my bank transactions file (bank-transactions.csv on my Desktop) for any payments matching the invoice amount in the past 30 days. If a matching payment exists, mark the invoice as "Possibly Paid - Verify" and include the transaction date. Save updated list as "overdue-invoices-checked.txt."

STEP 3 - Draft Follow-Ups:
For each invoice that is still overdue after Step 2 (not marked as possibly paid), draft a follow-up email. Tone: friendly but firm. Include the invoice number, amount, and original send date. For invoices 14-30 days overdue, use a gentle reminder. For invoices 30+ days overdue, use a firmer tone mentioning that payment is significantly past due. Save all drafts as "follow-up-drafts.txt" on my Desktop.

STEP 4 - Summary:
Create "invoice-follow-up-[today's date].md" with: total overdue amount, number of overdue invoices, list of follow-ups to send, and any invoices that may have been paid (need manual verification).
```

## Friday: hours, budgets, deadlines

This file is named `weekly-client-report-` so it won't overwrite the chapter 6 weekly check, which saves `weekly-report-` ([BOOK-FIXES.md](../../BOOK-FIXES.md)).

```
Complete the following workflow.

STEP 1 - Hours Compilation:
Read "time-tracking.csv" in my Google Drive. Sum hours by client for this week (Monday through today). Save as "weekly-hours.txt."

STEP 2 - Budget Check:
Read "client-budgets.csv" in my Google Drive. For each client in Step 1, compare hours used this week against remaining budget. Flag any client where this week's hours bring total hours above 80% of the budget cap. Save as "budget-status.txt."

STEP 3 - Deliverables Check:
Read my email for any messages this week containing the words "deliverable," "deadline," "due," or "submit." List them with client, subject, and date. Cross-reference with the calendar to identify any upcoming deadlines next week. Save as "deliverables-status.txt."

STEP 4 - Weekly Summary:
Compile into "weekly-client-report-[today's date].md" with: hours by client (with % of budget used), any budget warnings, upcoming deliverables and deadlines, and a list of next-week priorities based on deadlines and budget status.
```

## When a workflow breaks

Chapter 9 adds these to any workflow. The second goes after the last step, and the third before any step that changes a data file:

```
If any step fails (data source unavailable, file not found, connection error), note the failure in the final document and continue with the remaining steps. Do not stop the entire workflow because one step failed.
```

```
Review the completed document. Verify that each section contains data (not blank). If any section is empty, note 'DATA MISSING' and the likely cause.
```

```
Before making any changes to invoices.csv, save a copy as invoices-backup-[today's date].csv.
```

## Check

The final document is on your Desktop with every section filled, it uses at least three sources (calendar, email, files), and each step's own file is right when you open it.
