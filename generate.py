# -*- coding: UTF-8 -*-
import os,re,sys
import unicodedata
import unicodeblocks
blocks = {
    "Greek and Coptic": (0x0370, 0x03FF),
    "Mathematical Operators": (0x2200, 0x22FF), 
    "Miscellaneous Technical": (0x2300, 0x23FF),
    "Miscellaneous Mathematical Symbols-A": (0x27C0, 0x27EF),
    "Miscellaneous Mathematical Symbols-B": (0x2980, 0x29FF),
    "Supplemental Mathematical Operators": (0x2A00, 0x2AFF),
    "Mathematical Alphanumeric Symbols": (0x1D400, 0x1D7FF),
}

def processBlock(blockName, codeFrom, codeTo):
    fName = f"{blockName}.dic"
    f = open(fName, "w", encoding="utf-8")
    try:
        print(f"# {blockName}", file=f)
        for i in range(codeFrom, codeTo+1):
            c = chr(i)
            try:
                name = unicodedata.name(c)
            except ValueError:
                continue
            tokens = [
                c,
                name,
                "all",
                "never",
                f"# {c} {hex(i)}",
            ]
            s =  "\t".join(tokens)
            print(s, file=f)
    finally:
        f.close()
    os.system(f'python filter.py "{fName}"')
    os.system(f'python decap.py "{fName}"')

#for blockName, (codeFrom, codeTo) in blocks.items():
for name, block in unicodeblocks.blocks.items():
    print(f"{block.name}")
    processBlock(block.name, block.start, block.end)

#>>> print(unicodeblock.blocks.of('0'))
# print(blocks.of('α'))