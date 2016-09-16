import nltk
from nltk.corpus import wordnet as wn
import spellcheck

filepath = spellcheck.DATA+"/ambiguos-words"

def get_confusion_sets() :
    f = open(filepath, "r")
    l = []
    while (True) :
        s = f.readline()
        while (s=='\n') :
            s = f.readline()
        if (s=='EOF') :
            break
        x = []
        x.append(s.strip())
        s = f.readline()
        while (s != '\n') :
            x.append(s.strip())
            s = f.readline()
        l.append(x)
    return l

def is_ambiguous(word,l) :
    for k in l :
        if word in k :
            return True
    return False

def get_confusion_set(word) :
    l = get_confusion_sets()
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
        ans = 1.0
        for k in splits :
            syns1 = wn.synsets(word)
            syns2 = wn.synsets(k)
            print syns1
            print syns2
            print len(syns1) , len(syns2)
            if ((len(syns1)>0) & (len(syns2)>0)):
                w1 = wn.synset(syns1[0].name())
                w2 = wn.synset(syns2[0].name())
                x = w1.wup_similarity(w2)
                if (x != None) :
                    ans *= x

        d[word] = ans
    return d

d = correct_phrase("peace of cake")

print "\n\n\n\nThe final probabilities are : "
print d





