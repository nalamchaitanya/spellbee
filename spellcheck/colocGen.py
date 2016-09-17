import numpy
import spellcheck
from collections import defaultdict

def colocGen(filename):
    posDict = defaultdict(lambda:defaultdict(lambda:0))
    colocDict = defaultdict(lambda:defaultdict(lambda:0))
    for line in open(spellcheck.DATA+"/"+filename,'r'):
        list0 = line.strip().split("\t")
        count = int(line[0])

        tempDict = giveDict(list0[1:])
        for x,y in tempDict.items():
            posDict[x][y] += count

        tempList = giveCollocs(list0[1:])
        for x in tempList:
            colocDict[list0[1]][x] += count

    return (dict(posDict),dict(colocDict))



def giveDict(list0):
    temp = {}
    for i in range(0,3):
        temp[list0[i]] = list0[i+3]
    return temp

def giveCollocs(trigram):
    temp = []
    temp.append((trigram[0+3], ("_", trigram[1], trigram[2])))
    temp.append((trigram[1+3], (trigram[0], "_", trigram[2])))
    temp.append((trigram[2+3], (trigram[0], trigram[1], "_")))
    return temp

(p,c) = colocGen("w3ctest.txt")
print p,c