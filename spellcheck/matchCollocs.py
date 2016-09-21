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
    ind = words.index(am_words[0][0])
    confs = am_words[0][1]
    scoreConfs = {}
    scoreMax = 0
    suggWord = ""
    for word in confs:
        scoreConfs[word] = giveScore(ind,word,words)
        if scoreMax<scoreConfs[word]:
            scoreMax = scoreConfs[word]
            suggWord = word
    if(ind+1<len(words)):
        words.append("")
    string =" "
    return string.join(words[:ind])+" "+suggWord+" "+string.join(words[(ind+1):])

def giveScore(ind,word,words):
    posCollocs = givePossibleCollocs(ind,words)
    pos = givePos(word)
    scr=0
    print posCollocs
    for colloc in posCollocs:
        if (pos, colloc) in colocDict[word].keys():
            scr+=colocDict[word][(pos,colloc)]
    return scr

def givePossibleCollocs(ind,words):
    posSentencesDict = {}
    for w in words:
        posSentencesDict[w] = givePos(w)
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

sentence = "I would like to eat chocolate cake as desert"
print giveSuggestion(sentence)