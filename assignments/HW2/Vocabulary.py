import os
import string
from collections import defaultdict

import math

from assignments.HW2 import Ngramizer
from assignments.HW2 import SimpleTokenizer

class Vocabulary :
    path = '../../datasets/blogs/train/'
    MAX_FILES = math.inf;
    MAX_NGRAM = 3;




    corpusNgram = Ngramizer.Ngramizer()
    fCorpusNgram = Ngramizer.Ngramizer() #female corpussy
    mCorpusNgram = Ngramizer.Ngramizer() # female corpus

    amountFiles = 0;
    for filename in os.listdir(path):
        tokenizer = SimpleTokenizer.SimpleTokenizer()

        tokenizer.tokenizeFile(path,filename);


        words = tokenizer.getWords()

       # print("ngramize")  # print name of the file
        ngramizer = Ngramizer.Ngramizer()

        for i in range(1,MAX_NGRAM + 1) :
            ngramWords = ngramizer.ngramilize(words,i);

        corpusNgram.extend(ngramizer)

        if filename.startswith("F"): # is female corpus
            fCorpusNgram.extend(ngramizer)
        else :
            mCorpusNgram.extend(ngramizer)

        #stop at the maximum amount of files
        amountFiles += 1
        if amountFiles >= MAX_FILES :
            break


    corpusNgram.calcFrequencies()
    fCorpusNgram.calcFrequencies()
    mCorpusNgram.calcFrequencies()

    fCorpusNgram.createCorpusFile("F");
    mCorpusNgram.createCorpusFile("M");

    # n = 0;
    # for ngram in corpusNgram.ngrams :
    #     print("ngram" + str(n))
    #     frequencyList = frequencies(ngram);
    #     frequencyList = sorted(frequencyList.items(),key=lambda x: x[1], reverse=True)
    #     print("unique: " + str(len(frequencyList)))
    #     print(frequencyList[0:10])
    #
    #     if n is 0 :
    #         wordsList = list()
    #         for word in reversed(frequencyList) :
    #             if word[1] < 5 :
    #                 wordsList.append(word)
    #             else :
    #                 break
    #
    #         print(wordsList)
    #
    #     n += 1








