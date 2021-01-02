# -*- coding: UTF-8 -*-
import unicodedata
blocks = {
    "Greek and Coptic": (0x0370, 0x03FF),
}

def processBlock(blockName, codeFrom, codeTo):
    f = open(f"{blockName}.dic", "w", encoding="utf-8")
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

for blockName, (codeFrom, codeTo) in blocks.items():
    processBlock(blockName, codeFrom, codeTo)

#>>> print(unicodeblock.blocks.of('0'))
# print(blocks.of('α'))