# Decapitalizes unicode names
import os,re,sys

r = re.compile(r"\b([A-Z]{2,})\b")
fName = sys.argv[1]
#fName2 = sys.argv[2]
result = []
for s in open(fName, "r", encoding="utf-8").readlines():
    s = s.rstrip("\r\n")
    counter = 0
    while True:
        m = r.search(s)
        if m is None:
            break
        counter += 1
        if counter > 1000:
            raise Exception("Infinite loop!")
        word = m.group(0).lower()
        s = s[:m.start(0)] + word + s[m.end(0):]
    #print(s)
    result.append(s)

    
                
ff = open(fName, "w", encoding="utf-8")
try:
    print("\n".join(result), file=ff)
finally:
    ff.close()