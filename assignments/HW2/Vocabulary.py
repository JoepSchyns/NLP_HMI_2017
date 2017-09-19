import os
import string
from collections import defaultdict

import math

import Ngramizer
import SimpleTokenizer

class Vocabulary :
    path = '../../datasets/blogs/train/'
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
        print("open:" + filename) #print name of the file
        file = open(path + filename,encoding="utf8")

        text = file.read()

        print("tokenize")  # print name of the file
        tokenizer = SimpleTokenizer.SimpleTokenizer()
        tokenizer.tokenize(text)

        words = list()

        for token in tokenizer.tokenizedText :
            words.append(token[1])

        print("ngramize")  # print name of the file
        ngramizer = Ngramizer.Ngramizer()

        for i in range(1,MAX_NGRAM + 1) :
            ngramWords = ngramizer.ngramilize(words,i);
            #print(ngramWords);

        corpusNgram.extend(ngramizer)

        #stop at the maximum amount of files
        amountFiles += 1
        if amountFiles >= MAX_FILES :
            break


    for ngram in corpusNgram.ngrams :
        frequencyList = frequencies(ngram);
        frequencyList = sorted(frequencyList.items(),key=lambda x: x[1], reverse=True)
        print(frequencyList)







