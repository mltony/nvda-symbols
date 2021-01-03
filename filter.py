# Comments out characters already present in NVDA dictionary
import os,re,sys
nvdaSymbols = r"H:\drp\work\mltony\nvda\source\locale\en\symbols.dic"
nvdaChars = set()
for s in open(nvdaSymbols, "r", encoding="utf-8").readlines():
    s = s.rstrip("\r\n")
    if len(s) > 0:
        nvdaChars.add(s[0])
fName = sys.argv[1]
lines = open(fName, "r", encoding="utf-8").readlines()
f = open(fName, "w", encoding="utf-8")
try:
    for line in lines:
        line = line.rstrip("\r\n")
        if len(line) > 0 and line[0] in nvdaChars:
            line = "# " + line
        print(line, file=f)
finally:
    f.close()
