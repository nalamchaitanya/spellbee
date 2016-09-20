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
from nltk.corpus import stopwords
stwords = [str(x) for x in stopwords.words('english') if len(x)<=4]
print stwords
def file_as_list(f) :
    x = f.readline()
    l = []
    while (len(x)!=0) :
        l.append(x.strip())
        x = f.readline()
    return l
def removestopwords(s) :
    lis = s.split('\t')
    for k in stwords :
        while k in lis :
            lis.remove(k)
    ret = lis[0]
    if ('the' in lis) :
        print lis ,2
    for k in lis[1:] :
        ret += '\t'
        ret += k
    return ret

f = open(DATA+'/w2_.txt','r')
bigrams = file_as_list(f)
bigrams_ns = [removestopwords(k) for k in  bigrams ]
f.close()

f = open(DATA+'/w3_.txt','r')
trigrams = file_as_list(f)
trigrams_ns = [removestopwords(k) for k in trigrams]
f.close()

f = open(DATA+'/w4_.txt','r')
fourgrams = file_as_list(f)
fourgrams_ns =  [removestopwords(k) for k in fourgrams]
f.close()

#f = open(DATA+'/w5_.txt','r')
#fivegrams = file_as_list(f)
#fivegrams_ns =  [removestopwords(k) for k in fivegrams]
#f.close()