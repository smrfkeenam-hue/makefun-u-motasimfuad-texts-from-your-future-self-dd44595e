import os

# One funny text message from your future self: the dead plant is the
# fake one, and "Start there" lands the punch at the very end.
ENTRY = "Future you here. The plant died. The fake one. You killed a plastic plant. Start there."

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)


out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

