import spellcheck
import time
import pickle

from spellcheck.bktree import *

def divide(p,candidates123):
    candidates123[p[0] - 1] += [p[1]]
    return 1

#spellcheck.writecharXYcharsX()
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

print sorted(words_scores1, reverse=True)
print sorted(words_scores2, reverse=True)
print sorted(words_scores3, reverse=True)

end = time.time()
print (end-start)

