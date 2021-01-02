import os,re,sys

f3 = open(sys.argv[3], "w", encoding="utf-8")
goodChars = set()
for s in  open(sys.argv[1], "r", encoding="utf-8").readlines():
    s = s.rstrip("\r\n")
    print(s, file=f3)
    if not s.startswith("#"):
        goodChars.add(s[0])
print("# Other", file=f3)
for s in  open(sys.argv[2], "r", encoding="utf-8").readlines():
    s = s.rstrip("\r\n")
    if s[0] not in goodChars:
        print(s, file=f3)

f3.close()