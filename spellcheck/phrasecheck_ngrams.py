import time
from spellcheck import *
from nltk.corpus import stopwords
import string
import re
e = 2.43

stwords = [str(x) for x in stopwords.words('english') if len(x)<4]


def is_similar(ngram,phrase) :
    for word in ngram :
        if (word in phrase) :
            return True
    #for word in ngram :
    #    if (len(word)<3) :
    #        continue
    #    for pw in phrase :
    #       if ((word in pw)) :
    #            return True
    return False

def gen_trigrams(s) :
    ret = [s[i:i+3] for i in range(len(s)-2)]
    ret.sort()
    return ret

def similarity(s1,s2) :
    ret1 = gen_trigrams(s1)
    ret2 = gen_trigrams(s2)
    if (len(ret1)==0 | len(ret2)==0) :
        return 0.0
    ret  = [val for val in ret1 if val in ret2]
    l = len(ret)
    l1 = len(ret1)
    l2 = len(ret2)
    #print ret1,ret2,ret
    weight = float(5**l)/((float(5**abs(l2-l)))+float(3**abs(l1-l)))
    return weight

def solve(phrase) :
    all_list = []

    splits1 = phrase.split(' ')
    splits1 = [k for k in splits1 if len(k)!=0 if k not in stwords]
    joinedphrase = ''.join(splits1)

    ret = []
    lis = bigrams+trigrams+fourgrams
    lis_ns = bigrams_ns+trigrams_ns+fourgrams_ns

    st = time.time()
    print joinedphrase

    ff = open("results",'w')

    for i in range(len(lis_ns)) :
        splits2 = lis_ns[i].split('\t')

        val = float(splits2[0])
        splits2 = splits2[1:]
        if (is_similar(splits2,splits1)==False) :
            continue
        #print splits1,splits2
        joinedngram = ''.join(splits2)

        weight = similarity(joinedphrase,joinedngram)
        joinedngram += str(weight)
        ff.write(" "+joinedphrase+' '+joinedngram+'\n')
        ret.append((weight,val,lis[i]))

    ret.sort()
    ret.reverse()
    print ret


s= ""
print "enter in"
while(True) :
    s = raw_input()
    if (s=='end') :
        break
    solve(s)
#print similarity('roofhouse','roffhouse')
exit(0)