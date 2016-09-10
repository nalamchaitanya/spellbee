import os
import csv
import numpy

delMatrix = [];
subMatrix = [];
addMatrix = [];
revMatrix = [];

with open('../data/del.csv', 'r') as f:
    thedata = csv.reader(f)
    for row in thedata:
        temp=[];
        for elem in row:
            temp.append(int(elem));
        delMatrix.append(temp);

with open('../data/sub.csv', 'r') as f:
    thedata = csv.reader(f)
    for row in thedata:
        temp=[];
        for elem in row:
            temp.append(int(elem));
        subMatrix.append(temp);

with open('../data/add.csv', 'r') as f:
    thedata = csv.reader(f)
    for row in thedata:
        temp=[];
        for elem in row:
            temp.append(int(elem));
        addMatrix.append(temp);

with open('../data/rev.csv', 'r') as f:
    thedata = csv.reader(f)
    for row in thedata:
        temp=[];
        for elem in row:
            temp.append(int(elem));
        revMatrix.append(temp);

def delMat(x,y):
    return delMatrix[ord(x) - ord('a')][ord(y) - ord('a')];

def subMat(x,y):
    return subMatrix[ord(x) - ord('a')][ord(y) - ord('a')];

def addMat(x,y):
    return addMatrix[ord(x) - ord('a')][ord(y) - ord('a')];

def revMat(x,y):
    return revMatrix[ord(x) - ord('a')][ord(y) - ord('a')];