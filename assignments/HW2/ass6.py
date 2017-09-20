import os

import math

from assignments.HW2 import Ngramizer

from assignments.HW2 import SimpleTokenizer

PATH = "../../datasets/blogs/test/"

fNgramizer = Ngramizer.Ngramizer()
mNgramizer = Ngramizer.Ngramizer()

fNgramizer.readCorpus("F",3)
mNgramizer.readCorpus("M",3)

total = 0
positive = 0
negative = 0

rankingF = dict()
rankingM = dict()


def sortDictionary(dict):
    dictionary = dict
    dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    for i in range(0,10):
        print(dictionary[i])


for filename in os.listdir(PATH):
    total += 1
    tokenizer = SimpleTokenizer.SimpleTokenizer()
    tokenizer.tokenizeFile(PATH,filename)
    words = tokenizer.getWords()
    print(len(words))
    probF = fNgramizer.calculateTotalProb(words,0)
    probM = mNgramizer.calculateTotalProb(words,0)

    #rankingF = dict()
    #rankingM = dict()
    for word in fNgramizer.wordProb:
        rankingF[word] = fNgramizer.wordProb[word] / mNgramizer.wordProb[word]
        rankingM[word] = mNgramizer.wordProb[word] / fNgramizer.wordProb[word]

    print(filename)
    print("P(Female/Male)")
    sortDictionary(rankingF)
    print("P(Male/Female)")
    sortDictionary(rankingM)



    print("female: " + str(probF) + " male: " + str(probM))
    if probF > probM:
        print(filename + " Female ")
        if  filename.startswith("F") :
            positive += 1
        else:
            negative += 1

    else :
        print(filename + " Male ")
        if  filename.startswith("M") :
            positive += 1
        else:
            negative += 1

print("succes: " + str((positive / total) * 100) + "%")



