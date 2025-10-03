#!/usr/bin/env python3

import os

# Define your replacements
replacements = {
    "$DEF[FPGA]": "<tooltip>FPGA</tooltip>",
    "$DEF[SAR]": "<tooltip>SAR</tooltip>",
    "$DEFS[DTACQ]": "<tooltip>DTACQ</tooltip>",
    "$DEFS[GPL]": "<tooltip>GPL</tooltip>",
    "$DEFS[MDSplus]": "<tooltip>MDSplus</tooltip>",
    "$DEFS[EPICS]": "<tooltip>EPICS</tooltip>",
    "$DEFS[CSS]": "<tooltip>CSS</tooltip>",
    "$DEFS[dropbear]": "<tooltip>dropbear</tooltip>",
    "$DEFS[FPGA]": "<tooltip>FPGA</tooltip>",

    # Add more as needed
}

# Root folder relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.join(script_dir, "content")

for dirpath, _, filenames in os.walk(root_folder):
    for file in filenames:
        if file.endswith(".md"):
            filepath = os.path.join(dirpath, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            for old, new in replacements.items():
                content = content.replace(old, new)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

