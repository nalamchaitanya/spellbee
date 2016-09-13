import spellcheck
import time
import pickle

from spellcheck.bktree import *

def divide(p,candidates123):
    candidates123[p[0] - 1] += [p[1]]
    return 1

spellcheck.writecharXYcharsX()
#words = [line.strip() for line in open(spellcheck.DATA+"/dict.txt",'r')]

#tree = BKTree(levenshtein,dict_words(spellcheck.DATA+"/dict.txt"))
#pickle.dump(tree, open( "BKtree.p", "wb" ) )

spellcheck.readcharsXYcharsX()
tree=pickle.load(open("BKtree.p", "rb" ))
start = time.time()
word = "thruout"
candidates = tree.query(word, 3)
candidates123 = [[],[],[]]
map(lambda p: divide(p, candidates123), candidates)


print candidates123[0]
print candidates123[1]
print candidates123[2]

words_scores1 = map(lambda  p : (spellcheck.score(spellcheck.tranformation(word,p),p) , p ) ,candidates123[0])
words_scores2 = map(lambda  p : (spellcheck.score(spellcheck.tranformation(word,p),p) , p ) ,candidates123[1])
words_scores3 = map(lambda  p : (spellcheck.score(spellcheck.tranformation(word,p),p) , p ) ,candidates123[2])

words_scores1 = sorted(words_scores1, reverse=True)
words_scores2 = sorted(words_scores2, reverse=True)
words_scores3 = sorted(words_scores3, reverse=True)

'''

print spellcheck.jellyfish.metaphone(unicode(word,"utf-8"))
print map(lambda  s : (s,spellcheck.jellyfish.metaphone(unicode(s[1],"utf-8"))),words_scores1)
print map(lambda  s :(s,spellcheck.jellyfish.metaphone(unicode(s[1],"utf-8"))),words_scores2)
print map(lambda  s :(s,spellcheck.jellyfish.metaphone(unicode(s[1],"utf-8"))),words_scores3)

print spellcheck.jellyfish.soundex(unicode(word,"utf-8"))
print map(lambda  s : (s,spellcheck.jellyfish.soundex(unicode(s[1],"utf-8"))),words_scores1)
print map(lambda  s :(s,spellcheck.jellyfish.soundex(unicode(s[1],"utf-8"))),words_scores2)
print map(lambda  s :(s,spellcheck.jellyfish.soundex(unicode(s[1],"utf-8"))),words_scores3)


print spellcheck.jellyfish.match_rating_codex(unicode(word,"utf-8"))
print map(lambda  s : (s,spellcheck.jellyfish.match_rating_codex(unicode(s[1],"utf-8"))),words_scores1)
print map(lambda  s :(s,spellcheck.jellyfish.match_rating_codex(unicode(s[1],"utf-8"))),words_scores2)
print map(lambda  s :(s,spellcheck.jellyfish.match_rating_codex(unicode(s[1],"utf-8"))),words_scores3)


print spellcheck.jellyfish.nysiis(unicode(word,"utf-8"))
print map(lambda  s : (s,spellcheck.jellyfish.nysiis(unicode(s[1],"utf-8"))),words_scores1)
print map(lambda  s :(s,spellcheck.jellyfish.nysiis(unicode(s[1],"utf-8"))),words_scores2)
print map(lambda  s :(s,spellcheck.jellyfish.nysiis(unicode(s[1],"utf-8"))),words_scores3)

'''
end = time.time()
print (end-start)
