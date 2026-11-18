<!-- Chapter 7: Plugins and Skills That Give Claude Superpowers -->
# Chapter 7: Connectors, the file server, and skills

Connectors need no files from here: open Cowork's Customize area (or the "+" control in the chat) > Connectors, pick the service, sign in. The labels move between app versions, so look for "Customize", "+", "Connectors", "Extensions" and "Developer" wherever your version puts them.

## See the difference

The same calendar job, by screen and by connector:

```
Open Safari, go to calendar.google.com, wait for it to load, take a screenshot of tomorrow's date, read all the events from the screen, then open TextEdit, create a new document, type the list of meetings with times and attendees, and save it as "tomorrow-meetings.txt" on my Desktop.
```

```
Check my calendar for tomorrow. Save the list of meetings with times and attendees as "tomorrow-meetings.txt" on my Desktop.
```

## The filesystem server (optional)

The connected folders from chapter 3 already handle file tasks. This is a speed upgrade.

1. You need Node.js **version 24 or higher** for the current filesystem server (see [BOOK-FIXES.md](../../BOOK-FIXES.md)). To check, open Terminal and type `node --version`. If it's lower or missing, install the current version from nodejs.org. Terminal not for you? Skip this section; the connectors above don't need it.
2. In Claude, open Settings > Developer > Edit Config.
3. If the file that opens is empty, paste in all of [`claude_desktop_config.json`](claude_desktop_config.json). Change `username` to your Mac username and the two paths to the folders you want Claude to reach.
4. Save, then Command+Q and reopen Claude.

If your config already has an `mcpServers` section, don't paste a second one: A file with two `mcpServers` sections is broken JSON. Add only this entry inside the one you have, with a comma after the previous server's closing `}`:

```json
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Desktop",
        "/Users/username/Downloads"
      ]
    }
```

If the tools still don't show up after a restart, paste the whole file into any online JSON validator to find the missing comma or brace.

## Skills

Drag the three skill files onto your Desktop:

- [`skill-data-analyst.txt`](skill-data-analyst.txt): the chapter 6 audit, clean, report process
- [`skill-email-triage.txt`](skill-email-triage.txt): the chapter 5 triage, with archiving held back until you've checked it (a fix, see the file's second line)
- [`skill-meeting-notes.txt`](skill-meeting-notes.txt): decisions, owners, open questions

Start a conversation with one sentence and Claude works that way for the rest of it:

```
Read the file skill-data-analyst.txt on my Desktop and follow those instructions for this conversation.
```

Change the file name for the other two. If your Settings has a skills slot, use it instead. Its location changes between versions, so the book gives no path.

## Check what's installed

```
List the connectors, Extensions, and MCP servers you currently have access to and briefly describe what each one can do.
```

You're set when Claude can read your calendar, search the web, create a note in your notes app, and this prompt lists at least 3 connectors or Extensions.

## Before you install a new one

| Question | What to look for | Red flag |
|----------|-----------------|----------|
| Who made it? | Anthropic, the service provider (Google, Notion), or a well-known developer with a public GitHub profile | Anonymous developer, no source code available, no website |
| What permissions does it request? | Only what the plugin needs. A calendar plugin should ask for calendar access, not email and contacts | Requests permissions unrelated to its stated purpose |
| Is the code open-source? | Open-source means you (or someone you trust) can inspect exactly what the plugin does with your data | Closed-source from an unknown developer |
| Does it have documented setup instructions? | Clear README with installation steps, config examples, and troubleshooting | "Just install it and it works" with no documentation |
| How many people use it? | Check GitHub stars, Reddit mentions, or community reviews. More users means more eyes on potential problems | Zero community feedback or discussion |
| Does it duplicate a plugin you already have? | One plugin per category. Two calendar plugins will confuse Claude about which to use | You already have a working plugin in the same category |
| Can you test it on non-sensitive data first? | Create a test calendar event, a test note, a test file. Verify the result before trusting it with real work | The plugin requires access to sensitive data before you can test basic functionality |
