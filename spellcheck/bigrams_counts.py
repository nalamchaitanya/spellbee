import spellcheck
import re
import csv

def bigrams_count(filename):
    f = open(spellcheck.DATA + '/' + filename,'r')
    words = []
    line = f.readline()
    while line:
        if(line == ""):
            break
        line=line.split("\t")
        words += [(line[0].upper(),int(re.split("[A-Z]",line[1])[0]))]
        line=f.readline()
    sum = 0
    for p in words:
        sum += p[1]
    scale = float(sum)/float(44000000)
    bigramstemp = map (divide_word,words)
    bigrams =  [l for bi in bigramstemp for l in bi]
    unigrams = [(l,word[1]) for word in words for l in word[0]]
    charsXY = [[0]*26 for i in range(26)]
    charsX = [0]*26
    map(lambda p: increment(p,charsXY),bigrams)
    map(lambda p: increment1(p,charsX),unigrams)
    charsX = map(lambda p: float(p)/float(scale) ,charsX)
    charsXY = map(lambda ps: map(lambda p: float(p) / float(scale),ps), charsXY)
    wordfrequencies = map(lambda p : (p[0] , float(p[1])/float(scale) ),words)
    return (charsXY,charsX,wordfrequencies)

def increment(p,charsXY):
    charsXY[(ord(p[0][0]) - ord('A'))][(ord(p[0][1]) - ord('A'))] += p[1]
    return 1

def increment1(p,charsXY):
    charsXY[(ord(p[0][0]) - ord('A'))] += p[1]
    return 2

def divide_word(word):
    return [(word[0][s]+word[0][s+1] , word[1])  for s in range(len(word[0])-1)]


def writecharXYcharsX():
    (charsXY,charsX,wordfrqs) = bigrams_count("norvig.txt")
    target = open(spellcheck.DATA + '/charsXY.csv', 'wb')
    for i in range(26):
        target.write(str(charsXY[i][0]))
        for j in range(1,26):
            target.write(","+str(charsXY[i][j]))
        target.write("\n")
    target.close()
    target = open(spellcheck.DATA + '/charsX.csv', 'wb')
    target.write(str(charsX[0]))
    for i in range(1,26):
        target.write(","+str(charsX[i]))
    target.write("\n")
    target.close()
    target = open(spellcheck.DATA + '/wordfrequencies_scaled.csv', 'wb')
    target.write(wordfrqs[0][0] + "," + str(wordfrqs[0][1]))
    for i in range(len(wordfrqs)):
        target.write(wordfrqs[i][0] + "," + str(wordfrqs[i][1]))
        target.write("\n")
    target.close()

#def readcharsXYcharsX():

charsXY = [];
charsX = [];
wordfrqs = {};

def readcharsXYcharsX():
    with open(spellcheck.DATA + '/charsXY.csv', 'r') as f:
        thedata = csv.reader(f)
        for row in thedata:
            temp=[];
            for elem in row:
                temp.append(float(elem));
            charsXY.append(temp);

    with open(spellcheck.DATA + '/charsX.csv', 'r') as f:
        thedata = csv.reader(f)
        for row in thedata:
            for elem in row:
                charsX.append(float(elem));
    with open(spellcheck.DATA + '/wordfrequencies_scaled.csv', 'r') as f:
        thedata = csv.reader(f)
        for row in thedata:
            wordfrqs[row[0]] = float(re.split("[A-Z]",row[1])[0])

#charsXsum = sum(charsX)
#charsX = map(lambda p: p / float(charsXsum), charsX)
#charsXY = [map(lambda p: p / float(charsXsum), x) for x in charsXY]


            #   return (charsXY,charsX)


def charCount(x):
    return charsX[ord(x.upper())-ord('A')]

def charsCooc(x,y):
    return charsXY[ord(x.upper())-ord('A')][ord(y.upper())-ord('A')]

