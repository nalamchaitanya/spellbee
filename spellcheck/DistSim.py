import nltk
from nltk.corpus import brown


def smoothPMI(everyword_dists):
    for i i:
        for j in range(concepts):
            if(everyword_dists[i][j] == 0):
                everyword_dists[i][j] += 1
    noofconcepts = len(everyword_dists[0])
    words = len(everyword_dists)
    column_sums = map(lambda p : sum([i[p] for i in everyword_dists]) , range(noofconcepts)  )
    row_sums = map(lambda p: sum(p) , everyword_dists )
    for i in range(words):
        for j in range(noofconcepts):
            everyword_dists[i][j] = (everyword_dists[i][j] / (column_sums[i]*row_sums[j]))
    return everyword_dists


print brown.categories()
fdist = []
fdist = [nltk.FreqDist(w.lower() for w in brown.words(categories = i.decode('utf-8') )) for i in brown.categories()]
s = "piece cake"
s = s.split(" ")
everyword_dists = map(lambda  m : map(lambda p: p[m] ,fdist) , s)
for m in s:
    print m
    print map(lambda p: p[m] ,fdist)
everyword_dists = smoothPMI(everyword_dists)
#all_words = nltk.FreqDist(w.lower() for w in brown.words())
#print all_words['dessert']
print everyword_dists

sents = brown.sents(categories='news')
target=open('sample.txt','w')
for i in sents:
    target.write(str(i)+"\n")
target.close()


