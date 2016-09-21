import time
from spellcheck import *
from nltk.corpus import stopwords
import string
import re
import  copy
e = 2.43

def levenshtein(s, t):
    m, n = len(s), len(t)
    d = [range(n + 1)]
    d += [[i] for i in range(1, m + 1)]
    for i in range(0, m):
        for j in range(0, n):
            cost = 1
            if s[i] == t[j]: cost = 0

            d[i + 1].append(min(d[i][j + 1] + 1,  # deletion
                                d[i + 1][j] + 1,  # insertion
                                d[i][j] + cost)  # substitution
                            )
    return d[m][n]

def error_type(phraselist) :
    for k in phraselist :
        if (k not in words) :
            return SPELL_ERROR
    return CONTEXT_ERROR

def is_similar(ngram,phrase) :
    length = 0
    for word in ngram :
        for pp in phrase :
            if ((word in pp) | (pp in word)) :
                length += 1
                break
    if ((length >= len(phrase)-1) & (length!=0)) :
        return True
    return False

def gen_grams(s,n) :
    ret = [s[i:i+n] for i in range(len(s)-(n-1))]
    ret.sort()
    return ret

def similarity(s1,s2,n) :
    ret1 = gen_grams(s1,n)
    ret2 = gen_grams(s2,n)
    if (len(ret1)==0 | len(ret2)==0) :
        return 0.0
    ret  = [val for val in ret1 if val in ret2]
    l = len(ret)
    l1 = len(ret1)
    l2 = len(ret2)
    #print ret1,ret2,ret
    weight = float(2**l)/((float(3**abs(l2-l)))+float(3**abs(l1-l)))
    return weight

def spell_correct(phraselist,matches) :

    wrongword = ''
    suggestions = []
    print phraselist
    for i in range(len(phraselist)) :
        if (phraselist[i] not in words):
            wrongword = phraselist[i]
            print wrongword
            for match in matches :
                s = copy.copy(match[1])

                splitt = match[1].split('\t')
                matching = ''.join(splitt[1:])
                print wrongword,match[1]
                if (wrongword in matching) :
                    sp = s.split('\t')
                    correct = ' '.join(sp[1:])
                    phraselist[i] = correct
                    suggestions.append(phraselist)
                    return suggestions


    candidates = []
    index = 0
    for i in range(len(phraselist)):
        if (phraselist[i] not in words):
            wrongword = phraselist[i]
            index = i
            for match in matches:
                splits = match[1].split('\t')
                splits = splits[1:]
                for k in splits :
                    d = levenshtein(wrongword,k)
                    candidates.append((d,k))
            break
    candidates.sort()
    phraselist[index] = candidates[0][1]
    suggestions.append(phraselist)
    return suggestions

def solve(phrase) :

    splits_st = phrase.split(' ')
    splits1 = [k for k in splits_st if len(k)!=0 if k not in stwords]
    joinedphrase = ''.join(splits1)

    ret = []
    lis = bigrams+trigrams+fourgrams
    lis_ns = bigrams_ns+trigrams_ns+fourgrams_ns

    ff = open("results",'w')

    for i in range(len(lis_ns)) :
        splits2 = lis_ns[i].split('\t')

        val = float(splits2[0])
        splits2 = splits2[1:]
        if (is_similar(splits2,splits1)==False) :
            continue
        joinedngram = ''.join(splits2)

        weight = similarity(joinedphrase,joinedngram,3)*similarity(joinedphrase,joinedngram,4)
        joinedngram += str(weight)
        ff.write(" "+joinedphrase+' '+joinedngram+'\n')
        ret.append((weight*val,lis[i]))

    ret.sort()
    ret.reverse()
    print ret[:10]
    suggestions = ret[:2]
    if (error_type(splits_st)==SPELL_ERROR) :
        suggestions = spell_correct(splits_st,ret[:20])
    #else :
     #   suggestions = context_correct(splits_st,ret[:20])
    return suggestions


s= ""
print "enter in"
while(True) :
    s = raw_input()
    if (s=='end') :
        break
    print solve(s)

exit(0)