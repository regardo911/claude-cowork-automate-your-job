<!-- Chapter 6: Data Without the Data Science Degree -->
# Chapter 6: Clean a messy spreadsheet and get a report

You can run this on your own CSV or on [`test-data.csv`](test-data.csv), a 323-row practice file of made-up expenses with the chapter's main problems: three date formats, exact duplicates, near-duplicates, "see invoice" in the Amount column, empty dates, and names typed in different cases.

The practice file has an answer key, [`test-data-answers.md`](test-data-answers.md). Don't open it until Claude's audit is done. Then compare.

## Run it

Drag `test-data.csv` onto your Desktop. The practice dates are US style, so add this sentence to the end of the audit and clean prompts:

```
Interpret ambiguous dates as MM/DD/YYYY (US format).
```

Audit first. Nothing changes yet:

```
Read the file test-data.csv on my Desktop. Audit the data quality. Report the following: total number of rows, total number of columns with their names, data type of each column (dates, numbers, text), any data quality issues you find (duplicates, missing values, inconsistent formats, outliers, invalid entries). Do not fix anything yet. Just report what you find. Save the audit to a file called "data-audit.txt" on my Desktop.
```

Read `data-audit.txt` and decide how each problem gets handled. These are the book's rules; change any you disagree with:

```
Using the audit results, clean the data in test-data.csv. Apply these rules: 1) Standardize all dates to YYYY-MM-DD format. 2) Remove exact duplicate rows but keep near-duplicates and mark them with "REVIEW" in the Notes column. 3) Replace "see invoice" entries in Amount with 0 and add "MISSING AMOUNT" to Notes. 4) Standardize category names to Title Case. 5) Flag rows with empty dates by adding "MISSING DATE" to Notes. Save the cleaned data as "test-data-cleaned.csv" on my Desktop. Also save a cleaning log as "cleaning-log.txt" that records every change made, with the original value and the new value, so I can audit your work.
```

Then check the clean before you trust it. Put the number of "see invoice" rows from your own `cleaning-log.txt` where it says `[number]`:

```
Compare test-data.csv and test-data-cleaned.csv. Report: the row count before and after, the sum of the Amount column before and after, and every row where the Amount value changed. Confirm that the only intentional Amount changes are the [number] "see invoice" rows set to 0. Flag anything else.
```

The row count should drop by the removed duplicates and nothing else. Then the report:

```
Read test-data-cleaned.csv. Generate a report called "analysis-report.md" on my Desktop with the following sections: 1) Executive Summary (3-4 sentences for someone who will not read the full report). 2) Key Metrics (total transactions, total amount, average transaction, largest transaction, most common category, most common vendor). 3) Trends (monthly spending breakdown, top 5 categories by total spend, top 5 vendors by total spend). 4) Anomalies (any unusual patterns, the flagged items from the cleaning process, the outliers). 5) Recommendations (3-5 specific actions based on what the data shows). Write the entire report in plain English. No jargon. No statistical terms. A business owner with no data background should be able to read this and understand it.
```

You're done when `data-audit.txt`, `test-data-cleaned.csv`, `cleaning-log.txt` and `analysis-report.md` are on your Desktop and the numbers in them match the answer key (practice file) or a few rows you checked by hand (your file).

## On your own file

Swap `test-data.csv` and `test-data-cleaned.csv` for your file's names in every prompt, and change the column names in the clean and verify prompts (Amount, Notes) if yours are called something else. Work on a copy. If your dates are day-first (31/12/2025), add this line to the clean prompt:

```
Interpret as DD/MM/YYYY.
```

Add-ons for messier real files:

```
Strip currency symbols and commas from the Amount column. Convert all amounts to plain numbers with two decimal places.
```

```
Remove any completely empty rows. If you find header rows repeated in the middle of the data, remove the duplicates and keep only the first header row.
```

```
fill in any blank cells that are immediately below a non-blank cell with the same column heading, if the pattern suggests a merged-cell origin.
```

## Beyond one file

A week-over-week check of a "Weekly Reports" folder (chapter 8 shows how to schedule it):

```
Read the latest CSV in my "Weekly Reports" folder. Compare it to last week's data (the second-newest file in the same folder). Generate a week-over-week comparison report showing: total revenue change (dollar and percentage), top 3 categories that grew, top 3 categories that shrank, any new vendors or categories that did not exist last week, and any anomalies (transactions over $5,000, duplicate entries, missing data). Save the report as "weekly-report-[today's date].md" on my Desktop.
```

Free-text survey answers, for a `survey-results.csv` with a rating and a comment column:

```
Read survey-results.csv on my Desktop. Calculate the average rating. Then read every free-text comment and categorize each one into one of these buckets: Praise, Feature Request, Complaint, or Neutral. For complaints, identify the top 3 recurring themes. Generate a survey report with: overall satisfaction score, response breakdown by category, the top 3 complaint themes with 2-3 example quotes from actual responses, and 3 recommended actions based on the findings. Save as survey-report.md on my Desktop.
```

Matching bank transactions to invoices:

```
Read bank-transactions.csv and invoices.xlsx from my Desktop. Match transactions to invoices by comparing the Amount column in both files (allow a $0.50 difference for rounding). For matched pairs, create a new file called 'reconciliation.csv' with columns for Invoice Date, Client Name, Amount Due, Bank Date, Bank Description, and Status (mark as 'Matched'). List any unmatched bank transactions and unmatched invoices in separate sections at the bottom.
```
