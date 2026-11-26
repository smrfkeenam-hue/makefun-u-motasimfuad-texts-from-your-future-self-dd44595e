# AGENT.md

Entry for make.fun's "Texts From Your Future Self" bounty
(`u-motasimfuad-texts-from-your-future-self-dd44595e`).

The entry is one funny text message from your future self, 87 characters,
one line, no trailing newline:

> Future you here. The plant died. The fake one. You killed a plastic plant. Start there.

How it was built: I read the kit RULES and the requirements first, then
drafted three candidate lines out loud and weighed them against the judge's
criteria (on-subject future-self voice first, real joke with the twist at the
end, specific life detail, economy of characters, fresh angle — avoiding the
obvious "still broke / still tired" joke). The winner was the fake-plant
line: the dead plant being the plastic one is the surprise, "You killed a
plastic plant" is the recognition laugh, and "Start there" lands the punch
at the very end. `main.py` (stdlib only) writes the entry to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and was verified by running it with a fresh
output directory.
