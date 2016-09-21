import spellcheck
import time
import pickle

from spellcheck.bktree import *


#spellcheck.writecharXYcharsX()
words = set([line.strip() for line in open(spellcheck.DATA+"/dict.txt",'r')])
'''
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

'''
tree = BKTree(levenshtein,dict_words(spellcheck.DATA+'/dict.txt'))

'''


def divide(p,candidates123):
    if (p[1].isalpha()):
        candidates123[p[0] - 1] += [p[1]]
    return 1

#spellcheck.writecharXYcharsX()
#words = [line.strip() for line in open(spellcheck.DATA+"/dict.txt",'r')]

#tree = BKTree(levenshtein,dict_words(spellcheck.DATA+"/dict.txt"))
#pickle.dump(tree, open( "BKtree.p", "wb" ) )

spellcheck.readcharsXYcharsX()
tree=pickle.load(open("BKtree.pkl", "rb" ))
start = time.time()
word = "stupd"

candidates = tree.query(word, 3)
candidates123 = [[],[],[]]
map(lambda p: divide(p, candidates123), candidates)


#print candidates123[0]
#print candidates123[1]
#print candidates123[2]

candidates123[0] = spellcheck.prune_candidates(candidates123[0],word)
candidates123[1] = spellcheck.prune_candidates(candidates123[1],word)
candidates123[2] = spellcheck.prune_candidates(candidates123[2],word)

words_scores1 = map(lambda  p : ( spellcheck.score(spellcheck.tranformation(word,p),p)[0],spellcheck.score(spellcheck.tranformation(word,p),p)[1] , p ) ,candidates123[0])
words_scores2 = map(lambda  p : ( spellcheck.score(spellcheck.tranformation(word,p),p)[0] , spellcheck.score(spellcheck.tranformation(word,p),p)[1],p ) ,candidates123[1])
words_scores3 = map(lambda  p : ( spellcheck.score(spellcheck.tranformation(word,p),p)[0] ,spellcheck.score(spellcheck.tranformation(word,p),p)[1], p ) ,candidates123[2])

words_scores1 = sorted(words_scores1, reverse=True ,  key=lambda x: x[0])
words_scores2 = sorted(words_scores2, reverse=True ,  key=lambda x: x[0])
words_scores3 = sorted(words_scores3, reverse=True ,  key=lambda x: x[0])



final_word_list = spellcheck.merge_wordscores(words_scores1,words_scores2,words_scores3,word);

print final_word_list
#ggh
'''
print spellcheck.jellyfish.metaphone(unicode(word,"utf-8"))
print map(lambda  s : (s,spellcheck.jellyfish.metaphone(unicode(s[2],"utf-8"))),words_scores1)
print map(lambda  s :(s,spellcheck.jellyfish.metaphone(unicode(s[2],"utf-8"))),words_scores2)
print  map(lambda  s :(s,spellcheck.jellyfish.metaphone(unicode(s[2],"utf-8"))),words_scores3)


print spellcheck.jellyfish.soundex(unicode(word,"utf-8"))
print map(lambda  s : (s,spellcheck.jellyfish.soundex(unicode(s[2],"utf-8"))),words_scores1)
print map(lambda  s :(s,spellcheck.jellyfish.soundex(unicode(s[2],"utf-8"))),words_scores2)
print map(lambda  s :(s,spellcheck.jellyfish.soundex(unicode(s[2],"utf-8"))),words_scores3)


print spellcheck.jellyfish.match_rating_codex(unicode(word,"utf-8"))
print map(lambda  s : (s,spellcheck.jellyfish.match_rating_codex(unicode(s[2],"utf-8"))),words_scores1)
print map(lambda  s :(s,spellcheck.jellyfish.match_rating_codex(unicode(s[2],"utf-8"))),words_scores2)
print map(lambda  s :(s,spellcheck.jellyfish.match_rating_codex(unicode(s[2],"utf-8"))),words_scores3)


print spellcheck.jellyfish.nysiis(unicode(word,"utf-8"))
print map(lambda  s : (s,spellcheck.jellyfish.nysiis(unicode(s[2],"utf-8"))),words_scores1)
print map(lambda  s :(s,spellcheck.jellyfish.nysiis(unicode(s[2],"utf-8"))),words_scores2)
print map(lambda  s :(s,spellcheck.jellyfish.nysiis(unicode(s[2],"utf-8"))),words_scores3)
'''

end = time.time()
print (end-start)
