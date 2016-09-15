import os
import spellcheck


f = open(spellcheck.DATA+"/ambiguos-words","r") ;

l = []

fl = 0
while (fl==0) :
    x = []
    s = f.readline()
    while (s=='\n') :
        s = f.readline()
    x.append(s.strip())
    while (s != 'EOF') :
        s = f.readline()
        if (s=='\n') :
            break
        x.append(s.strip())
    if (s=='EOF') :
        fl = 1
    l.append(x)


l.remove(l[-1])
for k in l :
    print k