import spellcheck
import re
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
	bigramstemp = map (divide_word,words)
	bigrams =  [l for bi in bigramstemp for l in bi]
	unigrams = [(l,word[1]) for word in words for l in word[0]]
	charsXY = [[0]*26 for i in range(26)]
	charsX = [0]*26
	map(lambda p: increment(p,charsXY),bigrams)
	map(lambda p: increment1(p,charsX),unigrams)
	return (charsXY,charsX)

def increment(p,charsXY):
	charsXY[(ord(p[0][0]) - ord('A'))][(ord(p[0][1]) - ord('A'))] += p[1] 
	return 1

def increment1(p,charsXY):
	charsXY[(ord(p[0][0]) - ord('A'))] += p[1] 
	return 2

def divide_word(word):
	return [(word[0][s]+word[0][s+1] , word[1])  for s in range(len(word[0])-1)]  

(charsXY,charsX) = bigrams_count("norvig.txt")
