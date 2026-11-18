"""Checks that keep the files honest. Standard library only; CI runs it.

These check the files themselves (format, columns, the practice answer key,
links). None of them run a prompt: prompts run in Claude Desktop.
"""
import csv
import datetime
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CH = ROOT / "chapters"


def tracked_files():
    skip = {".git", "__pycache__"}
    return [p for p in ROOT.rglob("*") if p.is_file() and not (skip & set(p.parts))]


def fenced_blocks(md_text):
    blocks, cur, inside = [], [], False
    for line in md_text.splitlines():
        if line.startswith("```"):
            if inside:
                blocks.append("\n".join(cur))
                cur = []
            inside = not inside
            continue
        if inside:
            cur.append(line)
    return blocks


def header(path):
    with open(path, newline="") as f:
        return next(csv.reader(f))


# --- the practice spreadsheet ---------------------------------------------

DATE_FORMS = {
    "MM/DD/YYYY": (re.compile(r"^\d{2}/\d{2}/\d{4}$"), "%m/%d/%Y"),
    "DD-Mon-YY": (re.compile(r"^\d{2}-[A-Z][a-z]{2}-\d{2}$"), "%d-%b-%y"),
    "YYYY-MM-DD": (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "%Y-%m-%d"),
}


def parse_date(s):
    for rx, fmt in DATE_FORMS.values():
        if rx.match(s):
            return datetime.datetime.strptime(s, fmt).date()
    return None


def money(s):
    try:
        return float(s)
    except ValueError:
        return None


def practice_counts(path):
    """What a correct ch06 audit and clean should find, computed from the file."""
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    c = {"Rows in the file": len(rows)}
    for name, (rx, _) in DATE_FORMS.items():
        c[f"Dates written {name}"] = sum(1 for r in rows if rx.match(r["Date"]))
    c["Empty dates"] = sum(1 for r in rows if not r["Date"].strip())

    keyed = [tuple(r.values()) for r in rows]
    extra = len(keyed) - len(set(keyed))
    c["Exact duplicate rows (extra copies)"] = extra
    c["Rows after removing exact duplicates"] = len(rows) - extra

    see = [r for r in rows if r["Amount"].strip().lower().startswith("see invoice")]
    c['Amount cells that say "see invoice"'] = len(see)

    # dedupe in file order, as the clean step does
    seen, uniq = set(), []
    for r in rows:
        k = tuple(r.values())
        if k not in seen:
            seen.add(k)
            uniq.append(r)

    # near-duplicate: same vendor and amount, dates one day apart
    by_key = {}
    for i, r in enumerate(uniq):
        a, d = money(r["Amount"]), parse_date(r["Date"])
        if a is not None and d is not None:
            by_key.setdefault((r["Vendor"], a), []).append((d, i))
    pairs = set()
    for items in by_key.values():
        for d1, i1 in items:
            for d2, i2 in items:
                if i1 < i2 and abs((d1 - d2).days) == 1:
                    pairs.add((i1, i2))
    c["Near-duplicate pairs"] = len(pairs)
    c["Rows marked REVIEW after cleaning"] = len({i for p in pairs for i in p})

    spellings = {}
    for r in rows:
        spellings.setdefault(r["Vendor"].lower(), Counter())[r["Vendor"]] += 1
    varied = {k: v for k, v in spellings.items() if len(v) > 1}
    c["Vendors written in more than one case"] = len(varied)
    c["Rows with a vendor case variant"] = sum(sum(v.values()) - v.most_common(1)[0][1] for v in varied.values())

    c["Category cells not in Title Case"] = sum(1 for r in rows if r["Category"] != r["Category"].title())
    c["Dates the clean step rewrites to YYYY-MM-DD"] = sum(
        1 for r in uniq if r["Date"].strip() and not DATE_FORMS["YYYY-MM-DD"][0].match(r["Date"]))
    c["Rows marked MISSING DATE after cleaning"] = sum(1 for r in uniq if not r["Date"].strip())
    c["Rows marked MISSING AMOUNT after cleaning"] = sum(
        1 for r in uniq if r["Amount"].strip().lower().startswith("see invoice"))

    c["Amount total before cleaning (number cells only)"] = round(
        sum(money(r["Amount"]) or 0 for r in rows), 2)
    c["Amount total after cleaning"] = round(sum(money(r["Amount"]) or 0 for r in uniq), 2)
    return c


def answer_key(path):
    key = {}
    for line in path.read_text().splitlines():
        m = re.match(r"^\|\s*(.+?)\s*\|\s*([0-9][0-9,]*(?:\.[0-9]+)?)\s*\|\s*$", line)
        if m:
            key[m.group(1)] = float(m.group(2).replace(",", ""))
    return key


# spelled in two halves so this file passes its own check
BANNED = "rec" + "eipt"


class TestFiles(unittest.TestCase):

    def test_desktop_config_parses(self):
        cfg = json.loads((CH / "07-connectors-and-skills" / "claude_desktop_config.json").read_text())
        fs = cfg["mcpServers"]["filesystem"]
        self.assertEqual(fs["command"], "npx")
        self.assertIn("@modelcontextprotocol/server-filesystem", fs["args"])

    def test_starter_csv_columns_match_the_prompts(self):
        expect = {
            "09-workflows/invoices.csv": ["Invoice Number", "Client", "Invoice Date", "Amount", "Status"],
            "09-workflows/bank-transactions.csv": ["Date", "Description", "Amount"],
            "09-workflows/time-tracking.csv": ["Date", "Client", "Hours", "Notes"],
            "09-workflows/client-budgets.csv": ["Client", "Budget Hours", "Hours Used"],
            "12-your-workforce/client-rates.csv": ["Client Name", "Hourly Rate"],
            "06-spreadsheets/test-data.csv": ["Date", "Vendor", "Category", "Amount", "Invoice #",
                                              "Payment Method", "Notes"],
        }
        for rel, cols in expect.items():
            with self.subTest(rel):
                self.assertEqual(header(CH / rel), cols)

    def test_invoice_join_names_line_up(self):
        # ch12 joins time-tracking Client to client-rates Client Name
        def col(rel, name):
            with open(CH / rel, newline="") as f:
                return {r[name] for r in csv.DictReader(f)}
        tracked = col("09-workflows/time-tracking.csv", "Client")
        rated = col("12-your-workforce/client-rates.csv", "Client Name")
        self.assertTrue(tracked <= rated, tracked - rated)

    def test_practice_answer_key_is_true(self):
        folder = CH / "06-spreadsheets"
        truth = practice_counts(folder / "test-data.csv")
        key = answer_key(folder / "test-data-answers.md")
        self.assertEqual(set(key), set(truth), "answer key rows and checks differ")
        for label, value in truth.items():
            with self.subTest(label):
                self.assertAlmostEqual(key[label], value, places=2)
        self.assertEqual(truth["Rows after removing exact duplicates"],
                         truth["Rows in the file"] - truth["Exact duplicate rows (extra copies)"])
        self.assertGreaterEqual(truth["Rows in the file"], 50)  # ch06 BUILD STEP floor

    def test_template_file_matches_the_chapter_copies(self):
        text = (ROOT / "cowork-templates.txt").read_text()
        parts = re.split(r"^=== (Chapter (\d+): .+?) ===$", text, flags=re.M)
        found = 0
        for i in range(1, len(parts), 3):
            label, num, body = parts[i], parts[i + 1], parts[i + 2].strip("\n")
            folder = next(CH.glob(f"{int(num):02d}-*"))
            blocks = [b.strip("\n") for b in fenced_blocks((folder / "README.md").read_text())]
            with self.subTest(label):
                self.assertIn(body, blocks, f"{label} differs from {folder.name}/README.md")
            found += 1
        self.assertGreater(found, 20)

    def test_relative_links_resolve(self):
        link = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)|<img[^>]+src=\"([^\"]+)\"")
        for md in ROOT.rglob("*.md"):
            if ".git" in md.parts:
                continue
            for m in link.finditer(md.read_text()):
                target = m.group(1) or m.group(2)
                if re.match(r"^[a-z]+:", target):
                    continue
                with self.subTest(f"{md.relative_to(ROOT)} -> {target}"):
                    self.assertTrue((md.parent / target).exists())

    def test_no_banned_word_or_email_address(self):
        email = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}")
        for p in tracked_files():
            if p.suffix in {".png", ".pyc"}:
                continue
            text = p.read_text()
            with self.subTest(str(p.relative_to(ROOT))):
                self.assertNotIn(BANNED, text.lower())
                self.assertIsNone(email.search(text))


if __name__ == "__main__":
    unittest.main()
