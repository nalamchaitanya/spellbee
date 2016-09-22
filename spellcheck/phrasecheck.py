from nltk.corpus import wordnet as wn
import spellcheck
import operator
from nltk.corpus import stopwords

filepath = spellcheck.DATA+"/ambiguos-words"

def get_confusion_sets() :
    filepaths = [spellcheck.DATA+"/ambiguous-words",spellcheck.DATA+"/ambiguous-words22"]
    all_ls = [[],[]]
    for i in range(2):
        f = open(filepaths[i], "r")
        l = all_ls[i]
        while (True) :
            s = f.readline()
            while (s=='\n') :
                s = f.readline()
            if (s=='EOF') :
                break
            x = []
            x.append(s.strip())
            s = f.readline()
            while (s != '\n' and s!='EOF') :
                x.append(s.strip())
                s = f.readline()
            if(s =='EOF'):
                break
            l.append(x)
        print l
    l1 = all_ls[0]
    l2 = all_ls[1]
    for i in l1:
        for j in l2:
            if(len(list(set(i)&set(j)) ) >0):
                j = list(set(i+j))
                l1.remove(i)
                break;
    l = l1+l2
    return l

All_Confusion_sets = get_confusion_sets()

def is_ambiguous(word,l) :
    for k in l :
        if word in k :
            return True
    return False

def get_confusion_set(word) :
    l = All_Confusion_sets
    if (is_ambiguous(word,l)==False) :
        return [word]
    for k in l :
        if word in k :
            return k
    return []

def get_ambiguous_word(splits) :
    for word in splits :
        ret = get_confusion_set(word)
        if (len(ret)==1) :
            continue
        if (len(ret)>1) :
            return word
    return ""

def get_ambiguous_word_using_wordnet(phrase):
    splits = phrase.split(" ")
    word = checkspellerror(splits)
    if(word != -1):
        am_words = spellcheck.wordcheck.get_cadidates(word)
    return (word,am_words)

    #stpwords = [w for w in splits(" ") if w in stopwords.words('english')]
    filtered_splits = [w for w in splits if (( w not in stopwords.words('english')) or (len(w) > 4)) ]

    am_words = []   #collect all potential am_words
    for word in splits:
        ret = get_confusion_set(word)
        if (len(ret)==1) :
            continue
        if (len(ret)>1) :
            am_words += [(word,ret)]
    d = {}
    for confset in am_words:
        word = confset[0]
        confwords = confset[1]
        sim = 1
        for k in filtered_splits:
            if( k != word):
                total = sum(map(lambda p : word_net_similarity(p,k), confwords))
                if(total !=0):
                    ans = float(word_net_similarity(word,k)) / float(total)
                else :
                    ans =1
                sim +=ans
        d[word] = (confset[1],(float(sim)/float(len(filtered_splits))))
    print d
    sorted_x = sorted(d.items(), key=lambda x : x[1][1])
    sorted_x = [(i[0],i[1][0]) for i in sorted_x]
    print sorted_x
    return sorted_x


def correct_phrase(phrase) :
    splits = phrase.split(" ")
    ambigWord = get_ambiguous_word(splits)
    print ambigWord
    if (ambigWord=="") :
        return {}
    confset = get_confusion_set(ambigWord)
    splits.remove(ambigWord)
    d = {}
    for word in confset :
        sim = 1
        for k in splits :
            ans = word_net_similarity(word,k)
            if( ans != -1):
                sim +=ans
        d[word] = (float(sim)/float(len(splits)))
    return d

def word_net_similarity(word1,word2):
    syns1 = wn.synsets(word1)
    syns2 = wn.synsets(word2)
    #print (word1,syns1)
    #print (word2,syns2)

    if ((len(syns1) > 0) & (len(syns2) > 0)):
        w1 = wn.synset(syns1[0].name())
        w2 = wn.synset(syns2[0].name())
        x = w1.wup_similarity(w2)
        if (x != None):
            #print x
            return x
    return 0
'''
d = correct_phrase("peace of cake")

print "\n\n\n\nThe final probabilities are : "
print d
'''
#ggh
print len(All_Confusion_sets)
print All_Confusion_sets
import time
start = time.time()
phrase = "I would like the chocolate cake for desert"
word  = get_ambiguous_word_using_wordnet(phrase)
end = time.time()
print word
print (end-start)




