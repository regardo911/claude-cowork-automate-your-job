<!-- Chapter 4: Your First Real Task (Not "Hello World") -->
# Chapter 4: Audit and organize a messy folder

Pick a folder with 20 or more badly named files. Get its path from Finder: open the folder, turn on View > Show Path Bar, and copy the path from the bottom of the window. That path replaces `[your folder path]` in every prompt below.

Send them in this order and read each result before the next one. Claude looks first, you decide, then it moves files.

## 1. Look

```
Open Finder and go to [your folder path]. Audit every file in the folder. Create a document called "folder-audit.txt" on my Desktop with the following information for each file: the file name, the file type, the file size, and a one-sentence description of the content based on the file name (do not open the files yet, just describe what the name suggests). After the audit, suggest a folder structure with 4-6 subfolders based on the file types and apparent purposes you found.
```

Open `folder-audit.txt` on your Desktop. Rename the suggested subfolders to match how you think about the files.

## 2. Move

Put your subfolder names where it says `[list your folder names]`.

```
Now organize the files. Create the following subfolders inside [your folder path]: [list your folder names]. Move each file into the appropriate subfolder based on the audit. Do not rename any files. Leave files you are unsure about in a "Needs-Review" subfolder. When finished, update the folder-audit.txt file on my Desktop with the final file locations.
```

## 3. Write it up

```
Open the folder-audit.txt file on my Desktop. Based on the audit, create a new document called "folder-summary.md" on my Desktop with the following sections: an overview of the folder (total files, total size, file type breakdown), a list of the most important files with brief descriptions, any issues found (duplicate files, files with no extensions, files that might be outdated), and a recommended action list (files to delete, files to rename, files that need attention).
```

## Optional: read inside the files

Slower (Claude opens each PDF and Word file), but every file gets a real description.

```
Open each PDF and Word document in [your folder path]. For each file, read the first page and update the folder-audit.txt with a 2-3 sentence description of the actual content, not just the file name.
```

### Using the Google Drive connector instead

For the audit and the summary only, swap "Open Finder and go to [your folder path]" for "In my Google Drive, work with the folder named [folder name]". Do the move step in Finder with the Drive desktop app. Test a move on two throwaway files through the connector before you trust it with more (chapter 4, "The Right Way to Give Instructions").

## Check

- `folder-audit.txt` and `folder-summary.md` are on your Desktop.
- The original folder now holds your subfolders, plus `Needs-Review` for anything unclear.
- No file was renamed.

The same look, decide, act, check order runs every later chapter. Appendix A prints it as a fill-in pattern:

```
1. OBSERVE: "[Look at/Read] [data source]. Report what you find.
   Save the report as [filename] on my Desktop."
2. REVIEW: [You read the report and decide what to do]
3. ACT: "Using the report, [specific instructions for what to do].
   Do not [specific things to avoid]."
4. VERIFY: "Save a summary of what you did as [filename].
   Include any issues or items that need my attention."
```
