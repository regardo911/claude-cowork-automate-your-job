# Book fixes

The printed book can't change, so these are the places the files here differ from it, and why. Apart from these, file headers and one word swap in `email-rules.txt` ("order and payment confirmations"), the prompts and files match the book.

## Chapter 6: the sample cleaning log doesn't add up

The book prints "2,347 rows → 2,224 rows after cleanup" and "Exact Duplicates Removed: 34 rows". 2,347 − 34 = 2,313, not 2,224. Near-duplicates are flagged REVIEW and kept, so they don't come off the count. The chapter's own check says rows should drop by the removed duplicates only.

In this repo: the practice file's [answer key](chapters/06-spreadsheets/test-data-answers.md) adds up. 323 rows − 14 removed copies = 309, and a test recomputes every number in it from the CSV.

## Chapter 6: the verify prompt has the author's count in it

The book prints "Confirm that the only intentional Amount changes are the 14 "see invoice" rows set to 0." 14 is the author's file. Yours will be different.

In this repo: `the [number] "see invoice" rows`. Put in the count from your own `cleaning-log.txt` (11 for the practice file).

## Chapter 7: the email triage skill archives on the first run

The skill's step 4 says "Move emails in the ARCHIVE category out of the inbox." Chapter 5 says "Do not archive anything on this first run" and to use the "Claude-Archive-Review" label for "a week or two of runs" first.

In this repo: [`skill-email-triage.txt`](chapters/07-connectors-and-skills/skill-email-triage.txt) step 4 follows chapter 5. It labels the candidates. It archives only after a week or two of correct runs, and only with your OK.

## Chapter 7: the filesystem server needs Node 24

The book's check is "run `node --version`. If you see a version number, you are set". The current filesystem server asks for Node 24 or later:

```
$ npm view @modelcontextprotocol/server-filesystem version engines
version = '2.4.0'
engines = { node: '>=24' }
```

In this repo: the [chapter 7 page](chapters/07-connectors-and-skills/README.md) says the number has to be 24 or higher.

## Chapter 8: a missed run is not lost

"Handling Failures" says of a sleeping Mac: "The task simply does not run. There is no retry mechanism unless you build one." The same chapter's "The Laptop Problem" says Cowork "skips that run, then runs it automatically once you wake the machine or reopen the app", which is what Anthropic's help page on scheduled tasks says.

In this repo: the [chapter 8 page](chapters/08-scheduled-tasks/README.md) gives the second version.

## Chapter 9: two Friday reports share a file name with chapter 6

The chapter 6 weekly data check and the chapter 9 Friday Weekly Report both save `weekly-report-[today's date].md` on the Desktop. Run both on a Friday and the second overwrites the first.

In this repo: the chapter 9 Friday prompt saves `weekly-client-report-[today's date].md`. One name changed, nothing else.

## Chapter 12: the invoice generator doesn't line up with the chapter 9 files

The chapter 12 invoice prompt reads `time-tracking.csv` "from my Desktop" and `client-rates.csv` with a "Client Name" column. Chapter 9 keeps `time-tracking.csv` in Google Drive, with a "Client" column.

In this repo: the chapter 12 prompt reads `time-tracking.csv` "in my Google Drive", the same file chapter 9 uses, and adds one sentence: "Match the Client column in time-tracking.csv to Client Name in client-rates.csv." `client-rates.csv` keeps the printed columns and stays on the Desktop.
