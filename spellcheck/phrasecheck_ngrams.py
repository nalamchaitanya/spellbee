import time
from spellcheck import *
import  copy
import jellyfish as jf



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
        if  k not in words :
            return SPELL_ERROR
    return CONTEXT_ERROR

def is_similar(ngram,phrase) :
    length = 0
    for word in ngram :
        for pp in phrase :
            if (word in pp) | (pp in word):
                length += 1
                break
    if (length >= len(phrase)-1) & (length!=0):
        return True
    return False

def gen_grams(s,n) :
    ret = [s[i:i+n] for i in range(len(s)-(n-1))]
    ret.sort()
    return ret

def similarity(s1,s2,n) :
    ret1 = gen_grams(s1,n)
    ret2 = gen_grams(s2,n)
    if (len(ret1)==0) | (len(ret2)==0) :
        return 0.0
    ret  = [val for val in ret1 if val in ret2]
    l = len(ret)
    l1 = len(ret1)
    l2 = len(ret2)
    ##print  ret1,ret2,ret
    weight = float(2**l)/((float(3**abs(l2-l)))+float(3**abs(l1-l)))
    return weight

def spell_correct(phraselist,matches) :

    wrongword = ''
    suggestions = []
    fl = 0
    for i in range(len(phraselist)) :
        if phraselist[i] not in words:
            wrongword = phraselist[i]
            #print  wrongword
            for match in matches :
                s = copy.copy(match[1])

                splitt = match[1].split('\t')
                matching = ''.join(splitt[1:])
                #print  wrongword,match[1]
                if wrongword in matching :
                    sp = s.split('\t')
                    correct = ''
                    for x in sp :
                        if x in wrongword :
                            correct += x+' '
                    temp = copy.copy(phraselist)
                    temp[i] = correct
                    suggestions.append(temp)
                    fl = 1
                    break
            if fl ==1 :
                break

    candidates = []
    index = 0
    for i in range(len(phraselist)):
        if phraselist[i] not in words :
            wrongword = phraselist[i]
            index = i
            for match in matches:
                splits = match[1].split('\t')
                splits = splits[1:]
                #print splits
                for k in splits :
                    d = levenshtein(wrongword,k)
                    candidates.append((d,1.0/(1.0+jf.jaro_distance(k.decode('utf-8','ignore'),wrongword.decode('utf-8','ignore'))),k))


    candidates = list(set(candidates))
    candidates.sort()
    print candidates
    temp = copy.copy(phraselist)
    temp[index] = candidates[0][2]
    suggestions.append(temp)
    if len(suggestions)<2 :
        temp = copy.copy(phraselist)
        temp[index] = candidates[1][2]
        suggestions.append(temp)

    return suggestions

def compare_context(phraselist_nst,ngramlist) :
    baselist = [jf.match_rating_codex(k.decode('utf-8','ignore')) for k in ngramlist if k not in stwords]

    for wd in phraselist_nst :
        fl = 0
        phonetic = jf.match_rating_codex(wd.decode('utf-8','ignore'))
        for k in baselist :
            if (jf.levenshtein_distance(phonetic,k)<=1) :
                fl = 1
                break
        if (fl==0):
            return False
    return True



def context_correct(splits_st,splits_nst, matches):
    suggestions = [matches[i][1].split('\t')[1:] for i in range(2)]
    candidates = []
    for match in matches :
        val = float(match[0])
        wt = match[1][0].split('\t')[0]
        matching = match[1].split('\t')[1:]
        if compare_context(splits_nst,matching)==True :
            l = [k for k in splits_st if k in stwords if k in matching]
            l12 = [k for k in splits_st if k in stwords if k not in matching]
            l21 = [k for k in matching if k in stwords if k not in splits_st]
            val *= 3**(len(l)-len(l12)-len(l21))
            candidates.append((val,wt,matching))
    candidates.sort()
    candidates.reverse()
    if (len(candidates)>=2) :
        suggestions = [candidates[i][2] for i in range(2)]
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
        if is_similar(splits2,splits1)==False :
            continue
        joinedngram = ''.join(splits2)

        weight = similarity(joinedphrase,joinedngram,3)*similarity(joinedphrase,joinedngram,4)
        joinedngram += str(weight)
        ff.write(" "+joinedphrase+' '+joinedngram+'\n')
        ret.append((weight*val,lis[i]))

    ret.sort()
    ret.reverse()
    #print  ret[:10]
    suggestions = ret[:2]
    if error_type(splits_st)==SPELL_ERROR :
        suggestions = spell_correct(splits_st,ret[:20])
    else :
        suggestions = context_correct(splits_st,splits1,ret[:20])
    for k in suggestions:
        correct_phrase = ' '.join(k)
        print correct_phrase
    return suggestions

'''
s= ""
print  "enter input"
while True  :
    s = raw_input()
    if  s=='end' :
        break
    suggestions = solve(s)
    for k in suggestions :
        correct_phrase = ' '.join(k)
        print correct_phrase
'''

exit(0)