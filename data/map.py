import os

mapDict = {'da' : 'det' , 'da1' : 'det' , 'da2' : 'det' ,'dar' : 'det','dat' : 'det','db' : 'det','db2' : 'det',
           'dd' : 'det','dd1' : 'det','dd2' : 'det','ddq' : 'det','ddqge' : 'det','ddqv' : 'det' ,
           'if' : 'prep' ,'io' : 'prep','iw' : 'prep','ii' : 'prep','nno': 'nn', 'nnb': 'nn', 'nna': 'nn', 'nnu': 'nn',
           'np1': 'nn', 'np2': 'nn', 'nn': 'nn', 'nnl1': 'nn', 'nnl2': 'nn', 'np': 'nn', 'npm1': 'nn', 'nnu2': 'nn',
           'nnu1': 'nn', 'npm2': 'nn', 'nd1': 'nn', 'nn2': 'nn', 'nn1': 'nn', 'npd2': 'nn', 'npd1': 'nn', 'nnt1': 'nn',
           'nnt2': 'nn', 'nno2': 'nn','pphs2': 'prn', 'pn1': 'prn', 'pnqo': 'prn', 'ppio2': 'prn', 'ppis1': 'prn',
           'pph1': 'prn', 'ppis2': 'prn', 'ppho1': 'prn', 'ppho2': 'prn', 'pnqv': 'prn', 'ppge': 'prn', 'pnx1': 'prn',
           'pnqs': 'prn', 'ppy': 'prn', 'ppio1': 'prn', 'pn': 'prn', 'ppx1': 'prn', 'ppx2': 'prn', 'pphs1': 'prn',
           'rt': 'adv', 'rgq': 'adv', 'rex': 'adv', 'rgt': 'adv', 'rrqv': 'adv', 'rr': 'adv', 'rgr': 'adv',
            'rg': 'adv', 'rgqv': 'adv', 'ra': 'adv', 'rl': 'adv', 'rp': 'adv', 'rpk': 'adv', 'rrt': 'adv', 'rrr': 'adv',
            'rrq': 'adv'}

os.system("cp w3c1.txt temp")

for x,y in mapDict.items():
    os.system("sed \'s/"+x+"/"+y+"/g\' temp > temp1")
    os.system("mv temp1 temp")

os.system("mv temp w3c1.txt")