<!-- Chapter 8: Set It and Forget It (Recurring Tasks) -->
# Chapter 8: Three tasks that run every weekday

![Three scheduled tasks on a timeline. 6:00am email triage writes inbox-summary-[date].txt. 2:00pm data check compares weekly-sales.csv with weekly-sales-snapshot.csv, writes data-check-[date].txt and replaces the snapshot. 5:30pm end-of-day report reads both files and writes eod-report-[date].md. Each task adds a line to task-log.txt.](../../docs/images/daily-tasks.png)

Each scheduled task starts a fresh session with no memory of the others. The 5:30pm report knows what happened at 6:00am only because the morning task left a file on your Desktop.

## Before you schedule anything

Tick these off once now, and again whenever a task starts failing:

- [ ] The Mac is awake and Claude Desktop is open at the scheduled time.
- [ ] You're signed in to everything the task touches, with "stay signed in" on.
- [ ] Every connector the task uses shows connected in Settings, not "re-authenticate".
- [ ] Every file the prompt names exists at that exact path, in a connected folder.
- [ ] No update window, permission prompt or leftover save dialog is on screen.
- [ ] Nothing else is driving the screen at that moment.

Tasks run only while the Mac is awake and Claude is open. Chapter 8's "The Laptop Problem" gives three ways to keep it awake: turn off sleep while plugged in, schedule a wake, or use a spare Mac. No Schedule button for wake times on your Mac? This optional Terminal line from the chapter does the same job:

```
sudo pmset repeat wake MTWRF 05:45:00
```

Also add Claude Desktop to System Settings > General > Login Items so it opens when the Mac wakes.

## Task 1: 6:00am email triage

1. Type `/schedule` in the Cowork chat (or click Scheduled in the left sidebar, then + New task).
2. Name it "Morning email triage".
3. Paste the [chapter 5 triage prompt](../05-email-triage/README.md#paste-the-triage-prompt) into the prompt field. Put this sentence in front of it, so a logged-out browser stops the run instead of stalling it:

```
If Gmail shows a sign-in page, tell me in the chat and stop. Do not try to sign in.
```

4. Frequency: weekdays, 6:00am. Save.
5. Test it: set a copy for five minutes from now and check that the summary lands on your Desktop.

## Task 2: 2:00pm data check

Change `weekly-sales.csv` to the name of the file you want watched, in both places, and put a copy of it on your Desktop as the snapshot (or let the first run make one). Schedule at 2:00pm:

```
Read the file weekly-sales.csv in my Google Drive folder. Compare it to yesterday's snapshot (saved as weekly-sales-snapshot.csv on my Desktop). Report any changes: new rows added, rows deleted, values that changed (show old vs new value). If no changes were found, just say "No changes since yesterday." Save the comparison as "data-check-[today's date].txt" on my Desktop. Then replace the snapshot file with the current version so tomorrow's comparison uses today's data.
```

To reset the baseline after changes you made on purpose, delete the snapshot file.

## Task 3: 5:30pm end-of-day report

Schedule at 5:30pm. Put this at the start of the prompt, so a missing morning file gets reported instead of skipped quietly:

```
First, check if inbox-summary-[today's date].txt and data-check-[today's date].txt exist on my Desktop. If either is missing, note which one is missing in the report and proceed with the data you have.
```

```
Compile an end-of-day report and save it as "eod-report-[today's date].md" on my Desktop. Include: 1) Summary of today's email activity (how many processed, how many sent, any urgent items still pending). 2) Calendar summary for tomorrow (list meetings with times). 3) Action items from today that are still open (check the inbox summary and data check from earlier today). 4) Any files Claude created or modified today (list with brief description).
```

## Know what ran

Add this as the last sentence of all three prompts:

```
Append a line to the file task-log.txt on my Desktop with the format: [date] [time] [task name] [status: SUCCESS/FAIL] [summary].
```

## If a run is missed

If the Mac was asleep or Claude was closed at 6:00am, the run is skipped. It starts by itself when you wake the Mac or open Claude, and it shows in the task history. (The book contradicts itself here: see [BOOK-FIXES.md](../../BOOK-FIXES.md).) A run can also fail while the Mac is awake, for example the internet was down or Gmail logged you out. Check `task-log.txt`. If the morning file is missing, paste the prompt by hand.

## Check

All three tasks have run at least once and left their files on your Desktop: the inbox summary, a `data-check-` file, an `eod-report-` file, and three SUCCESS lines in `task-log.txt`.
