from nltk.corpus import wordnet as wn
import spellcheck
import operator

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

def get_ambiguous_word_using_wordnet(phrase) :
    splits = phrase.split(" ")
    d = {}
    for word in splits :
        sim = 1
        for k in splits:
            if( k != word):
                ans = word_net_similarity(word,k)
                if( ans != -1):
                    sim +=ans
        d[word] = (float(sim)/float(len(splits)))

    print d
    sorted_x = sorted(d.items(), key=operator.itemgetter(1))
    sorted_x = [i[0] for i in sorted_x]
    print sorted_x
    am_words = []
    for word in sorted_x :
        ret = get_confusion_set(word)
        if (len(ret)==1) :
            continue
        if (len(ret)>1) :
            am_words += [(word,d[word])]
    return am_words


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
    print (word1,syns1)
    print (word2,syns2)

    if ((len(syns1) > 0) & (len(syns2) > 0)):
        w1 = wn.synset(syns1[0].name())
        w2 = wn.synset(syns2[0].name())
        x = w1.wup_similarity(w2)
        if (x != None):
            print x
            return x
    return -1

d = correct_phrase("peace of cake")

print "\n\n\n\nThe final probabilities are : "
print d

#ggh
phrase = "I do sometimes need just a moment of rest and piece"
word  = get_ambiguous_word_using_wordnet(phrase)
print word





