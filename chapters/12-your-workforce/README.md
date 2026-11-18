<!-- Chapter 12: Your AI Workforce Starts Today -->
# Chapter 12: Five more workflows

Fill the brackets in each one, run it by hand once, then schedule it.

### Competitive price monitor (daily, 9am)

```
Complete the following steps. STEP 1: Open Safari and go to [competitor URL 1]. Find the price of [product name]. Save to "price-check.csv" on my Desktop with columns: Date, Competitor, Product, Price. STEP 2: Repeat for [competitor URL 2] and [competitor URL 3]. STEP 3: Compare today's prices to yesterday's "price-snapshot.csv" on my Desktop. Report any changes (price increases or decreases) with the dollar and percentage difference. STEP 4: Save today's data as the new "price-snapshot.csv" for tomorrow's comparison. Save the comparison as "price-alert-[today's date].txt."
```

### Tenant or client email triage

Drag [`tenant-rules.txt`](tenant-rules.txt) onto your Desktop and put in your tenant names and your own urgency words.

```
Read tenant-rules.txt on my Desktop. Open my email. Read all unread emails from tenants (any sender matching a name in tenant-rules.txt). Categorize each email: MAINTENANCE REQUEST (include urgency: low/medium/high based on keywords), RENT QUESTION, LEASE QUESTION, GENERAL. For maintenance requests, draft a response with an estimated timeline based on urgency. Save summary as "tenant-summary-[today's date].txt."
```

### Social media drafts

```
STEP 1: Search the web for the top 5 trending articles in [your industry] published in the past 7 days. Save the titles, URLs, and a 1-sentence summary of each as "trending-content.txt" on my Desktop. STEP 2: For each article, draft a social media post (under 280 characters for Twitter, under 500 characters for LinkedIn) that references the article's key insight and ties it to [your business or expertise]. STEP 3: Save all drafts as "social-drafts-[today's date].txt" with the format: Platform, Draft Text, Source URL.
```

### Student or team progress tracker (weekly)

```
STEP 1: Open Safari and go to [Google Classroom / shared spreadsheet / project board URL]. Read all submissions or updates from the past 7 days. STEP 2: For each person, note: name, items submitted, items overdue, last activity date. STEP 3: Save as "progress-report-[today's date].md" with sections: On Track (submitted everything), Needs Attention (1-2 items overdue), At Risk (3+ items overdue or no activity in 7+ days). Include a count for each category.
```

### Invoices from your hours (every two weeks)

This prompt reads `time-tracking.csv` from Google Drive (the file the [chapter 9 Friday report](../09-workflows/README.md) uses) and [`client-rates.csv`](client-rates.csv) from your Desktop. The printed prompt looked for the time file on the Desktop and never said how the client columns match ([BOOK-FIXES.md](../../BOOK-FIXES.md)). Spell each client name the same in both files.

```
STEP 1: Read "time-tracking.csv" in my Google Drive. Sum hours by client for the past 2 weeks. STEP 2: Read "client-rates.csv" from my Desktop (columns: Client Name, Hourly Rate). Match the Client column in time-tracking.csv to Client Name in client-rates.csv. Calculate the invoice amount for each client (hours x rate). STEP 3: For each client, create a file called "invoice-[client name]-[today's date].txt" on my Desktop with: my business name and address, client name, invoice date, hours worked, hourly rate, total amount, and payment terms (Net 30). STEP 4: Save a summary as "invoice-batch-[today's date].md" listing all invoices generated with amounts.
```

## Days 22 to 25

Days 22 to 25 of the book's plan build a template library. [`cowork-templates.txt`](../../cowork-templates.txt) holds 34 of the book's prompts, chapters 4 to 12. Drag it onto your Desktop and add a note under each prompt as you learn its run time and what breaks it.
