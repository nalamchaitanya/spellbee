import os

PROJECT_DIR=os.pardir
DATA=PROJECT_DIR+"/data"
from confusion import *
from bigrams_counts import *
from wordcheck import *
from scoring import *

words=set()
# if __name__ == "__main__":
#     spellcheck.words = set(spellcheck.get_dictionary('norvig.txt'))
#     print spellcheck.gen_candidates('god')
# print 'hi'
editsex = [("sub",('a','c'))]
# print editsex[0][1][0]
print spellcheck.score(editsex)
# temp = spellcheck.charCount(editsex[0][1][1])
# print temp
# print charsX
