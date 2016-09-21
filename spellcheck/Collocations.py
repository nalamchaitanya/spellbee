import spellcheck

Word_tags = {'peace' : [('nn1',0.8) , ('npl',0.2) ], 'piece' : [('nn1',0.5) , ('npl',0.5) ] }
Word_collocs = {}

def All_POS_taggs(sentence,errword):
    #nltk_tag= spellcheck.nltk.pos_tag(sentence)
    #print nltk_tag
    words = sentence.split(" ")
    tag_sequences = []
    i = words.index(errword)
    start = max(0,i-2)
    end = min(i+2,len(words))
    tag_list = map(lambda p : word_tags(Word_tags[p])  , words[start:(end)])
    print tag_list
    for i in range(start,max(1,end-2)):
        tag_sequences += get_possible_tags(tag_list , (i-start) ,min(3,len(tag_list)))
    return tag_sequences

def word_tags(list):
    if (list[0][1] > 0.6):
        return [list[0]]
    return [list[0], list[1]]

def get_possible_tags(tag_list , index, length):
    if(length == 0):
        return []
    next_tags = get_possible_tags(tag_list,index+1,length-1)
    if (next_tags == []):
        return map(lambda p : ([p[0]] , p[1]) , tag_list[index])
    possible_tags = []
    for tag in tag_list[index]:
        possible_tags += map(lambda p : ([tag[0]] + p[0] , tag[1]*p[1] ),next_tags)
    return possible_tags

def Features_extraction_selection(confusion_set):
    features = {}
    for word in confusion_set:
        Collocations = map(lambda p : (p[1],Word_tags[word][p]) , Word_tags[word].keys())
        for colloc in Collocations:
            if colloc[0] in features:
                features[colloc[0]][word] = colloc[1]
            else:
                features[colloc[0]] =({word :colloc[1]})
    all_collocs = features.keys()

    Mi = 0
    for word in confusion_set:
        Mi += sum(Word_tags[word].values())  # total frequency of word i

    colloc_frequency = []
    threshold =10
    for colloc in all_collocs:
        if(sum(colloc.values()) < threshold ):
            del features[colloc]
        else:
            if(sum(colloc.values() - Mi )  < threshold):
                del features[colloc]
            else:
                colloc_frequency += [(colloc, sum(colloc.values()))]
                for word in confusion_set:
                    if word not in colloc.keys():
                        colloc[word] = 0;
    #features obtained each sum values also obtained


    colloc_strength = map(lambda p : (p[0] , float(max(features[p[0]].values))/float(p[1]))  , colloc_frequency)
    colloc_strength = sorted(colloc_strength, reverse=True ,key = lambda x : x[1])
    return (features , colloc_strength)


sentence='peace piece'
print All_POS_taggs(sentence,'piece')














