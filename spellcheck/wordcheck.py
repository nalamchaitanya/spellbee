import spellcheck
import time

from spellcheck.bktree import *

#spellcheck.writecharXYcharsX()
words = set([line.strip() for line in open(spellcheck.DATA+"/dict.txt",'r')])

def firstPrefix(word) :
    prefix = ''
    ret = []
    for i in range(len(word)) :
        prefix += word[i]
        if (prefix in words) :
            ret.append(prefix)
    return ret

list = []
index = 0
def split1(word,l) :
    #global list
    if (len(word)==0) :
        list.append([])
        for k in l :
            list[-1].append(k)
        print l
        return
    ret = firstPrefix(word)
    for k in ret :
        l.append(k)
        xx = word[len(k):]
        split1(xx,l)
        #list.append(l)
        l.remove(l[-1])


split1('halloffame',[])
print list


'''
tree = BKTree(levenshtein,dict_words(spellcheck.DATA+'/dict.txt'))

print time.time()
print tree.query("rajiv", 3)
print time.time()
'''

