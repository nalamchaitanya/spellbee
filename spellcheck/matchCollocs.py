from colocGen import *
import operator
import spellcheck

confSet = {"desert":["desert","dessert"],"dessert":["desert","dessert"]}
#(posDict,colocDict) = colocGen("w3ctest.txt")
posDict =pickle.load(open('POSdict.pkl', 'rb'))
colocDict = pickle.load(open('Colocdict.pkl', 'rb'))

def giveConfusionWord(words):
    index = len(words)-1
    return index

def giveSuggestion(sentence):
    words = sentence.split(" ")
    am_words = spellcheck.get_ambiguous_word_using_wordnet(sentence)
    print am_words
    i = 0
    while (i<len(am_words)):
        ind = words.index(am_words[i][0])
        confs = am_words[i][1]
        scoreConfs = {}
        scoreMax = 0
        suggWord = ""
        for word in confs:
            scoreConfs[word] = giveScore(ind,word,words)
            print scoreConfs[word]
            if scoreMax<scoreConfs[word]:
                scoreMax = scoreConfs[word]
                suggWord = word
        if(ind+1<len(words)):
            words.append("")
        string =" "
        print suggWord
        if(suggWord != words[ind]):
            break
        i +=1
        print words
        words = sentence.split(" ")
    return string.join(words[:ind])+" "+suggWord+" "+string.join(words[(ind+1):])

def giveScore(ind,word,words):
    posCollocs = givePossibleCollocs(ind,words)
    pos = givePos(word)
    scr=0
    print (word,pos,posCollocs)
    for colloc in posCollocs:
        if (pos, colloc) in colocDict[word].keys():
            scr+=colocDict[word][(pos,colloc)]
        else :
            scr += float(sum(posDict[word].values()))/float(len(colocDict[word]))
    return scr/float(sum(posDict[word].values()))

def givePossibleCollocs(ind,words):
    #posSentencesDict = {}
    #for w in words:
    #    posSentencesDict[w] = givePos(w)
    #ind = words.index(word)
    colocList = []
    if(ind+2<len(words)):
        colocList.append(("_",givePos(words[ind+1]),givePos(words[ind+2])))
    if(ind+1<len(words) and ind>0):
        colocList.append((givePos(words[ind-1]),"_",givePos(words[ind+1])))
    if(ind>1):
        colocList.append((givePos(words[ind-2]),givePos(words[ind-1]),"_"))
    return colocList

def givePos(word):
    posList = posDict[word]
    return sorted(posList.items(),key=operator.itemgetter(1),reverse=True)[0][0]

import time
start = time.time()
sentence = "The parliament passed the resoltion to discuss the bil"
print giveSuggestion(sentence)
end = time.time()
print (end-start)