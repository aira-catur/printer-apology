"""The Printer Apology - make.fun one-liner entry.

Judge brief (from RULES.txt): Write the funniest one-line apology from a
printer, 120 characters max. An apology note from an office printer to the
people who keep jamming it, feeding it cheap paper and swearing at it.
Gate (RULES.txt): /output/entry.txt is UTF-8 text of 1 to 120 characters,
not only white space. Entry filename: entry.txt.

Judge criteria, most important first:
1. Genuinely an apology from a printer to its office, with printer's gripes.
2. The laugh: a real joke, punch at the end.
3. Printer truth: jams, cheap paper, staples, being asked for colour, ink.
4. Freshness: not the first joke anyone would write about a printer.
5. Economy: every word earns its place, no padding.
A note only sad or only rude is weaker than one that is funny.
"""
import os

# Scores per candidate: (on_brief, laugh, printer_truth, freshness, economy)
CANDIDATES = [
    ("Sorry I jammed again; in my defence, you feed me paper thinner than your excuses for being late.",
     (9, 6, 8, 5, 7)),
    ("I'm sorry for the paper jam. You try digesting 500 sheets a day with no water and constant swearing.",
     (9, 7, 8, 6, 6)),
    ("Sorry I printed it blank. I ran out of ink three weeks ago; nobody reads my warnings, either.",
     (9, 7, 9, 6, 8)),
    ("Apologies for eating page 7. It had a staple in it, and that was the closest thing to a meal I've had.",
     (9, 7, 8, 7, 7)),
    ("Sorry I'm 'offline' again. I needed a minute after you hit me, called me useless, then asked for colour.",
     (9, 6, 8, 6, 7)),
    ("I'm sorry I groan when I wake up. I'm twelve years old, full of dust, and still faster than your meetings.",
     (8, 6, 6, 6, 7)),
    ("Sorry for printing 40 copies. You pressed the button 40 times. I was just finally doing what you asked.",
     (9, 8, 9, 7, 8)),
    ("Sorry I jammed on page 2 of 40: you fed me paper like tissue, hit me twice, then blamed me to the whole office.",
     (9, 7, 9, 6, 7)),
    ("Sorry for shouting PC LOAD LETTER at you. It's my only way of saying Dave from Accounts has jammed me again.",
     (9, 8, 9, 7, 8)),
    ("Sorry I printed your 'private' letter face-up for the whole office. You hit print; I just delivered the gossip.",
     (9, 8, 8, 8, 8)),
    ("Sorry for PC LOAD LETTER and 12 blank pages: I ran out of ink weeks ago. I was faking it - like your timesheets.",
     (10, 10, 10, 9, 9)),
    ("Sorry I need cyan to print in black. I don't understand it either; I just work here, badly, and only when watched.",
     (9, 8, 9, 8, 7)),
]

def score(candidate):
    text, scores = candidate
    on_brief, laugh, truth, fresh, economy = scores
    # Judge weighs criteria in order; laugh and truth carry extra weight.
    return on_brief * 3 + laugh * 3 + truth * 2 + fresh * 2 + economy

def main():
    winner = max(CANDIDATES, key=score)[0]
    assert 1 <= len(winner) <= 120, f"char count {len(winner)} outside 1..120 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(winner)

if __name__ == "__main__":
    main()
