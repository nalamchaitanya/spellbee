import nltk
from nltk.corpus import brown
import math

def smoothPMI(everyword_dists):
    noofconcepts = len(everyword_dists[0])
    words = len(everyword_dists)
    for i in range(words):
        for j in range(noofconcepts):
            if(everyword_dists[i][j] == 0):
                everyword_dists[i][j] += 1
    column_sums = map(lambda p : sum([i[p] for i in everyword_dists]) , range(noofconcepts)  )
    row_sums = map(lambda p: sum(p) , everyword_dists )
    for i in range(words):
        for j in range(noofconcepts):
            everyword_dists[i][j] = (float(everyword_dists[i][j]) / float((column_sums[j]*row_sums[i])))
    return everyword_dists

def VectorSimilarity(list1,list2):
    ip = sum(map(lambda p: list1[p] * list2[p], range(len(list1))))
    i1 = math.sqrt(sum( [i*i for i in list1]))
    i2 = math.sqrt(sum([i*i for i in list2]))
    return (float(ip)/float(i1*i2))
print brown.categories()
fdist = []
fdist = [nltk.FreqDist(w.lower() for w in brown.words(categories = i.decode('utf-8') )) for i in brown.categories()]
s = "I would like chocolate cake for desert"
s = s.split(" ")
fdists = map(lambda  m : map(lambda p: p[m] ,fdist) , s)
for m in range(len(s)):
    print s[m]
    print fdists[m]

everyword_dists = smoothPMI(fdists)
for m in range(len(s)):
    print s[m]
    print everyword_dists[m]


Words_sim = {}
for m in everyword_dists:
    sim = 0
    for j in everyword_dists:
        if(j != m):
            sim+=VectorSimilarity(m,j)
    Words_sim[s[everyword_dists.index(m)]]=sim
print Words_sim
#all_words = nltk.FreqDist(w.lower() for w in brown.words())
#print all_words['dessert']

sents = brown.sents(categories='news')
target=open('sample.txt','w')
for i in sents:
    target.write(str(i)+"\n")
target.close()


