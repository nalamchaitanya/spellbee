from collections import defaultdict

import pickle
def colocGen(filename):
    posDict = defaultdict(lambda:defaultdict(lambda:0))
    colocDict = defaultdict(lambda:defaultdict(lambda:0))
    for line in open("../data/"+filename,'r'):
        list0 = line.strip().split("\t")
        count = int(line[0])

        tempDict = giveDict(list0[1:])
        for x,y in tempDict.items():
            posDict[x][y] += count

        tempList = giveCollocs(list0[1:])
        for i in range(0,3):
            colocDict[list0[i+1]][tempList[i]] += count

    return (dict(posDict),dict(colocDict))


def giveDict(list0):
    temp = {}
    for i in range(0,3):
        temp[list0[i]] = list0[i+3]
    return temp

def giveCollocs(trigram):
    temp = []
    temp.append((trigram[0+3], ("_", trigram[1+3], trigram[2+3])))
    temp.append((trigram[1+3], (trigram[0+3], "_", trigram[2+3])))
    temp.append((trigram[2+3], (trigram[0+3], trigram[1+3], "_")))
    return temp

(p,c) = colocGen("w3c.txt")

newp = {}
for x,y in p.items():
    newp[x] = dict(y)

newc = {}
for x,y in c.items():
    newc[x] = dict(y)

with open('POSdict.pkl', 'wb') as handle:
  pickle.dump(newp, handle)
with open('Colocdict.pkl', 'wb') as handle:
  pickle.dump(newc, handle)

