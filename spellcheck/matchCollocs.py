from colocGen import *
import operator

confSet = {"desert":["desert","dessert"],"dessert":["desert","dessert"]}
(posDict,colocDict) = colocGen("w3ctest.txt")

def giveConfusionWord(words):
    index = len(words)-1
    return index

def giveSuggestion(sentence):
    words = sentence.split(" ")
    ind = giveConfusionWord(words)
    confs = confSet[words[ind]]
    scoreConfs = {}
    scoreMax = 0
    suggWord = ""
    for word in confs:
        scoreConfs[word] = giveScore(word,words)
        if scoreMax<scoreConfs[word]:
            scoreMax = scoreConfs[word]
            suggWord = word
    if(ind+1<len(words)):
        words.append("")
    return words[:ind].join(" ")+" "+suggWord+" "+words[(ind+1):].join(" ")

def giveScore(word,words):
    posCollocs = givePossibleCollocs(word,words)
    pos = givePos(word)
    scr=0
    for colloc in posCollocs:
        scr+=colocDict[word][(pos,colloc)]
    return scr

def givePossibleCollocs(word,words):
    posSentencesDict = {}
    for w in words:
        posSentencesDict[w] = givePos(w)
    ind = words.index(word)
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
    return sorted(posList.items(),operator.itemgetter(1),reverse=True)[0][0]

sentence = "I would like to eat chocolate cake as desert."