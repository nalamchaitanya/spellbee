import spellcheck

def score(edits):
    res = 1
    for edit in edits:
        if edit[0]== "sub":
            res *= spellcheck.subMat(edit[1][0], edit[1][1])/float(spellcheck.charCount(edit[1][1]))
        elif edit[0]== "del":
            res *= spellcheck.delMat(edit[1][0], edit[1][1]) / float(spellcheck.charsCooc(edit[1][0], edit[1][1]))
        elif edit[0] == "add":
            res *= spellcheck.addMat(edit[1][0], edit[1][1]) / float(spellcheck.charCount(edit[1][0]))
        elif edit[0] == "rev":
            res *= spellcheck.revMat(edit[1][0], edit[1][1]) / float(spellcheck.charsCooc(edit[1][0], edit[1][1]))
    return res

