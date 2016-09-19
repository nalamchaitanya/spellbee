import time

from spellcheck import *
from nltk.corpus import stopwords
import re

stwords = [str(x) for x in stopwords.words('english') if len(x)<=4]
print stwords
def get_gist(s) :
    s1 = re.split(r'[\s\t]',s)
    ret = []
    for k in s1 :
        if (k not in stwords) :
            ret.append(k)
    #print ret
    return ''.join(ret)
def filter(s) :
    s = re.sub(r'[^\w]','',s)
    s.replace("\t","")
    s.replace(" ","")
    return s ;
def gen_trigrams(s) :
    ret = [hash(s[i:i+3]) for i in range(len(s)-2)]
    ret.sort()
    return ret

def similarity(s1,s2) :
    ret1 = gen_trigrams(s1)
    ret2 = gen_trigrams(s2)
    if (len(ret1)==0 | len(ret2)==0) :
        return 0.0
    ret  = [val for val in s1 if val in s2]
    return float(len(ret))/(len(ret1)+len(ret2))

d = {}
l = []
st = time.time()
phrase = 'wate fountain at paris'
spl = phrase.split(" ")
splits2 = [k for k in spl if k not in stwords]
for x in bigrams+trigrams+fourgrams+fivegrams :
    x = str(x)
    splits = x.split("\t")
    freq   = float(splits[0])
    splits1 = [k for k in splits[1:] if k not in stwords]
    isection = [k for k in splits2 if k in splits1]

    if (len(isection)==0) :
        continue
    actual = ""
    for k in splits[1:] :
        actual += k+"\t"
    actual = get_gist(actual)
    phrase = get_gist(phrase)
    #print actual,phrase
    weight = similarity(filter(actual),filter(phrase))
    l.append((weight,str(x)))
en = time.time()

l.sort()
l.reverse()
for k in l:
    print k
print (en-st)
'''
weight = similarity(filter('hewasparticularlyinterested'),filter('interestedparticlarly'))
print weight
print get_gist('he	was	particularly	interested')
'''
