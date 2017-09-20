import os

import math

from assignments.HW2 import Ngramizer

from assignments.HW2 import SimpleTokenizer

PATH = "../../datasets/blogs/test/"

fNgramizer = Ngramizer.Ngramizer()
mNgramizer = Ngramizer.Ngramizer()

fNgramizer.readCorpus("F",3)
mNgramizer.readCorpus("M",3)



for filename in os.listdir(PATH):
    tokenizer = SimpleTokenizer.SimpleTokenizer()
    tokenizer.tokenizeFile(PATH,filename)
    words = tokenizer.getWords()

    probF = fNgramizer.calculateTotalProb(words,1)
    probM = mNgramizer.calculateTotalProb(words,1)
    print("female: " + str(probF) + " male: " + str(probM))
    if probF > probM:
        print(filename + " Female ")
    else :
        print(filename + " Male ")



