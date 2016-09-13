import os

PROJECT_DIR=os.pardir
DATA=PROJECT_DIR+"/data"
from confusion import *
#from bigrams_counts import *
#from wordcheck import *
from scoring import *
import time

# if __name__ == "__main__":
#     spellcheck.words = set(spellcheck.get_dictionary('norvig.txt'))
#     print spellcheck.gen_candidates('god')
# print 'hi'

# print editsex[0][1][0]


#(charsXY,charsX) = spellcheck.readcharsXYcharsX()


# temp = spellcheck.charCount(editsex[0][1][1])
# print temp
# print charsX
