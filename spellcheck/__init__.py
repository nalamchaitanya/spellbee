import os
import jellyfish
#from confusion import *
from bigrams_counts import *


PROJECT_DIR=os.pardir
DATA=PROJECT_DIR+"/data"
from confusion import *
from bigrams_counts import *
#from wordcheck import *
from scoring import *

f = open(DATA+'/w2_.txt','r')
bigrams = [x.strip() for x in f.readlines()]
f.close()

f = open(DATA+'/w3_.txt','r')
trigrams = [x.strip() for x in f.readlines()]
f.close()

f = open(DATA+'/w4_.txt','r')
fourgrams = [x.strip() for x in f.readlines()]
f.close()

f = open(DATA+'/w5_.txt','r')
fivegrams = [x.strip() for x in f.readlines()]
f.close()
