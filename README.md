# Claude Cowork - Automate Your Job This Weekend

**Your inbox sorted and replies drafted before you open your laptop. Then the rest of your desk work.**

Companion files for the book *Claude Cowork - Automate Your Job This Weekend*, from [youcanbuildthings.com](https://youcanbuildthings.com).

These are the book's prompts and Desktop files, one folder per chapter, so you copy instead of retype. Every prompt runs in your own Claude Desktop on a Pro or Max plan: paste it into Cowork and Claude does the work on your Mac. Two terms show up right away. **Computer Use** lets Claude see your screen and click and type for you (chapter 3). **Connectors** link Claude straight to Gmail, Google Drive, Calendar and Slack (chapters 5 and 7). Pick your line below.

[![CI](https://github.com/regardo911/claude-cowork-automate-your-job/actions/workflows/ci.yml/badge.svg)](https://github.com/regardo911/claude-cowork-automate-your-job/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) · Educational material, not advice: [DISCLAIMER.md](DISCLAIMER.md)

<img src="docs/images/hero.png" width="896" alt="The book's prompts and Desktop files, by chapter. Left: an example inbox-summary text file from chapter 5 with URGENT (3), NEEDS YOUR REPLY (8) with draft replies ready, FYI ONLY (47) and ARCHIVE CANDIDATES (69) labelled Claude-Archive-Review, waiting on the Desktop when the 6:00 task finishes. Right: where each file goes. email-rules.txt to the Desktop, chapter 5. The three skill files to the Desktop, chapter 7. claude_desktop_config.json into Settings, Developer, Edit Config, chapter 7. test-data.csv to the Desktop for practice, chapter 6. Three daily task prompts into the /schedule prompt field, chapter 8. Three workflow prompts into the Cowork chat, chapter 9. cowork-templates.txt to the Desktop, chapters 4 to 12. Bottom: download the ZIP from the green Code button, no terminal.">

## Start here

### "I want Claude sorting my inbox tomorrow morning"

1. At the top of this page, click the green **Code** button, then **Download ZIP**. Double-click the ZIP in your Downloads folder to open it. No GitHub account needed.
2. Drag `chapters/05-email-triage/email-rules.txt` onto your Desktop. Open it and replace each bracket with your own senders: your boss and key clients under URGENT, your bank and doctor under SKIP. The [chapter 5 page](chapters/05-email-triage/README.md) goes through every bracket.
3. Sign in to your email in the browser, then paste the [triage prompt](chapters/05-email-triage/README.md#paste-the-triage-prompt) into the Cowork chat.
4. Look on your Desktop for `inbox-summary-` and today's date: your urgent mail, draft replies, and FYI list. Archive candidates get the Gmail label `Claude-Archive-Review` for you to check. The prompt tells Claude not to archive or send anything.
5. Type `/schedule` in the chat, paste the same prompt, and set it for weekdays at 6:00am ([chapter 8](chapters/08-scheduled-tasks/README.md)).

If Claude describes the steps instead of doing them, turn on Computer Use first ([chapter 3](chapters/03-get-it-running/README.md)).

### "I'm working through the book"

Open the chapter you're on in the [chapter map](#chapter-map). Each page has that chapter's prompts with a copy button, and what you should see when it worked.

### "I want to practice the spreadsheet chapter without my own data"

Drag [`chapters/06-spreadsheets/test-data.csv`](chapters/06-spreadsheets/test-data.csv) onto your Desktop and paste the [chapter 6 audit prompt](chapters/06-spreadsheets/README.md#run-it). The file is made-up practice data. When Claude finishes, [`test-data-answers.md`](chapters/06-spreadsheets/test-data-answers.md) tells you what it should have found.

### "I finished the book and want the files"

Use the copy table below, or take [`cowork-templates.txt`](cowork-templates.txt): all 34 reusable prompts in one file, by chapter.

## Where each file goes

| Chapter | File | Where it goes on your Mac |
|---|---|---|
| 5 | [`email-rules.txt`](chapters/05-email-triage/email-rules.txt) | Desktop |
| 6 | [`test-data.csv`](chapters/06-spreadsheets/test-data.csv) | Desktop, for practice |
| 7 | [`skill-data-analyst.txt`](chapters/07-connectors-and-skills/skill-data-analyst.txt), [`skill-email-triage.txt`](chapters/07-connectors-and-skills/skill-email-triage.txt), [`skill-meeting-notes.txt`](chapters/07-connectors-and-skills/skill-meeting-notes.txt) | Desktop |
| 7 | [`claude_desktop_config.json`](chapters/07-connectors-and-skills/claude_desktop_config.json) | Claude > Settings > Developer > Edit Config (optional) |
| 8 | The data check and end-of-day prompts, plus the chapter 5 triage prompt | The `/schedule` prompt field |
| 9 | [`invoices.csv`](chapters/09-workflows/invoices.csv) | An Accounting folder in Google Drive |
| 9 | [`bank-transactions.csv`](chapters/09-workflows/bank-transactions.csv) | Desktop |
| 9 | [`time-tracking.csv`](chapters/09-workflows/time-tracking.csv), [`client-budgets.csv`](chapters/09-workflows/client-budgets.csv) | Google Drive |
| 11 | The Safe Mode prefix | The Cowork chat, in front of any new prompt |
| 12 | [`tenant-rules.txt`](chapters/12-your-workforce/tenant-rules.txt), [`client-rates.csv`](chapters/12-your-workforce/client-rates.csv) | Desktop |
| All | [`cowork-templates.txt`](cowork-templates.txt) | Desktop |
| All | Every other prompt on the chapter pages | The Cowork chat |

The CSVs in chapters 9 and 12 hold three fake rows each to show the format. Put your own rows in.

## Chapter map

Chapters 1 and 2 have nothing to copy.

| Chapter | What you build | It worked when |
|---|---|---|
| [3. Zero to running](chapters/03-get-it-running/README.md) | Computer Use switched on | `cowork-test.txt` is on your Desktop and Claude told you the temperature |
| [4. First real task](chapters/04-folder-audit/README.md) | An organized folder and a summary | `folder-audit.txt` and `folder-summary.md` on your Desktop, files in subfolders, none renamed |
| [5. The email machine](chapters/05-email-triage/README.md) | Morning triage with draft replies | An inbox summary on your Desktop and archive candidates under `Claude-Archive-Review` |
| [6. Data](chapters/06-spreadsheets/README.md) | A cleaned spreadsheet and a plain-English report | Audit, cleaned CSV, cleaning log and report on your Desktop, counts matching the answer key |
| [7. Plugins and skills](chapters/07-connectors-and-skills/README.md) | Connectors, the file server, 3 skills | Claude lists at least 3 connectors or Extensions |
| [8. Recurring tasks](chapters/08-scheduled-tasks/README.md) | 6:00am, 2:00pm and 5:30pm tasks | Each task left its file on your Desktop and a SUCCESS line in `task-log.txt` |
| [9. Workflows](chapters/09-workflows/README.md) | One chained workflow | One finished document built from calendar, email and files |
| [10. Income](chapters/10-side-income/README.md) | A listing, or a smarter job search | A listing is live, a job batch went out, or a prompt ran on a real client job |
| [11. Stay safe](chapters/11-stay-safe/README.md) | The three rules and a No-AI folder | `access-test.txt` shows the No-AI folder as SKIPPED |
| [12. Your workforce](chapters/12-your-workforce/README.md) | Five more workflows | Each one's file lands on your Desktop |

Where the repo differs from the printed book, [BOOK-FIXES.md](BOOK-FIXES.md) lists the change and the reason.

## What you need

- A Mac on macOS 11 (Big Sur) or later.
- Claude Desktop, from claude.ai/download.
- A Claude Pro or Max plan. Computer Use is on Pro and Max only, so a work Team or Enterprise login won't show the setting (chapter 3).
- Node.js 24 or higher, only if you add the optional filesystem server in chapter 7.

## Contributing

Found a prompt that doesn't match your copy of the book, or a mistake that belongs in BOOK-FIXES.md? Open an issue (it needs a free GitHub account) and name the chapter. Every file here maps to one.

## License

MIT, see [LICENSE](LICENSE).

Educational material only. Claude acts on your Mac, so read each prompt before you run it. Full text in [DISCLAIMER.md](DISCLAIMER.md).
