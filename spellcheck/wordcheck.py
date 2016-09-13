import spellcheck
import time

from spellcheck.bktree import *

words = [line.strip() for line in open(spellcheck.DATA+"/dict.txt",'r')]

tree = BKTree(levenshtein,dict_words(spellcheck.DATA+'/dict.txt'))

print time.time()
print tree.query("rajiv", 2)
print time.time()


