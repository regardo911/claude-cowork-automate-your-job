# Answer key for test-data.csv

Every vendor and row in `test-data.csv` is made up.

What a correct run of the chapter 6 prompts should find in the practice file. Check Claude's `data-audit.txt` and `cleaning-log.txt` against it. Claude may word things differently or group them another way; the counts are what matter.

## In the file as you downloaded it

| Check | Count |
|---|---|
| Rows in the file | 323 |
| Dates written MM/DD/YYYY | 192 |
| Dates written DD-Mon-YY | 63 |
| Dates written YYYY-MM-DD | 59 |
| Empty dates | 9 |
| Exact duplicate rows (extra copies) | 14 |
| Amount cells that say "see invoice" | 11 |
| Near-duplicate pairs | 9 |
| Vendors written in more than one case | 9 |
| Rows with a vendor case variant | 16 |
| Category cells not in Title Case | 24 |
| Amount total before cleaning (number cells only) | 328,062.66 |

Exact duplicates: 14 rows each appear twice, every column identical. Near-duplicates: same vendor and same amount, dates one day apart, so a person should look at them. A vendor case variant is a row like `acme test co` or `MOCK SOFTWARE INC` where most rows say `Acme Test Co` or `Mock Software Inc`. The chapter 6 prompt doesn't define a near-duplicate, so Claude may count them differently. Check the rows it flagged.

## After the book's five cleaning rules

| Check | Count |
|---|---|
| Rows after removing exact duplicates | 309 |
| Dates the clean step rewrites to YYYY-MM-DD | 246 |
| Rows marked REVIEW after cleaning | 18 |
| Rows marked MISSING DATE after cleaning | 9 |
| Rows marked MISSING AMOUNT after cleaning | 11 |
| Amount total after cleaning | 309,057.60 |

323 rows minus 14 removed copies is 309. In the verify prompt, `[number]` is 11. The Amount total drops by 19,005.06, the money in the 14 removed copies. The 11 "see invoice" cells become 0, so they change nothing.

If Claude's counts differ, ask it to list the rows behind the number it reported. That's usually where the miss is.
