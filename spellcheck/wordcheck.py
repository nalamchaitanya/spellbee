import spellcheck
import time

from spellcheck.bktree import *

words = [line.strip() for line in open(spellcheck.DATA+"/dict.txt",'r')]

tree = BKTree(levenshtein,dict_words('/home/rajiv/CodingIsFun/spellbee/data/dict.txt'))

print time.time()
print tree.query("rajiv", 2)
print time.time()


