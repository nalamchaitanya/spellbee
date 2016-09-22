import os
import spellcheck
import jellyfish


s = u'piece'
s1 = jellyfish.match_rating_codex(u'place').lower().decode('utf-8','ignore')
s2 = jellyfish.match_rating_codex(u'plaid').lower().decode('utf-8','ignore')
print s1 , s2
print jellyfish.levenshtein_distance(s1,s2)

#print jellyfish.levenshtein_distance(s,u'thruout')
