import os
import string
from collections import defaultdict

import math

import Ngramizer
import SimpleTokenizer

class Vocabulary :
    path = '../../datasets/blogs/train/'
    corpusFile = "../../datasets/blogs/ngramCorpus.txt"
    MAX_FILES = math.inf;
    MAX_NGRAM = 3;

    def frequencies(list):

        frequencyList = defaultdict(int)
        for item in list:
            frequencyList[item] += 1

        return frequencyList




    corpusNgram = Ngramizer.Ngramizer();

    amountFiles = 0;
    for filename in os.listdir(path):
        #print("open:" + filename) #print name of the file
        file = open(path + filename,encoding="utf8")

        text = file.read()

       # print("tokenize")  # print name of the file
        tokenizer = SimpleTokenizer.SimpleTokenizer()
        tokenizer.tokenize(text)

        words = list()

        for token in tokenizer.tokenizedText :
            words.append(token[1])

       # print("ngramize")  # print name of the file
        ngramizer = Ngramizer.Ngramizer()

        for i in range(1,MAX_NGRAM + 1) :
            ngramWords = ngramizer.ngramilize(words,i);

        corpusNgram.extend(ngramizer)

        #stop at the maximum amount of files
        amountFiles += 1
        if amountFiles >= MAX_FILES :
            break




    n = 0
    for ngram in corpusNgram.ngrams :
        file = open(corpusFile + str(n), 'w+')
        frequencyList = frequencies(ngram);
        frequencyList = sorted(frequencyList.items(), key=lambda x: x[1], reverse=True)
        for word in frequencyList :
            file.write("%s\n" % str(word))

        n += 1
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








