import null as null

import spellcheck

f = open(spellcheck.DATA+'/norvig.txt','r')
words = []
while 1 :
    line = f.readline()
    if (line == null):
        break
    wordmap = line.split("\t")
    words.append(wordmap[0])
