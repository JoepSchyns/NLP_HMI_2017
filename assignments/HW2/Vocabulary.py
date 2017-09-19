import os
import string
from collections import defaultdict

import Ngramizer
import SimpleTokenizer

class Vocabulary :
    path = '../../datasets/blogs/train/'
    MAX_FILES = 1;

    def frequencies(list):

        frequencyList = defaultdict(int)
        for item in list:
            frequencyList[item] += 1

        return frequencyList


    tokenizer = SimpleTokenizer.SimpleTokenizer()
    ngramizer = Ngramizer.Ngramizer()

    allWords = list()

    amountFiles = 0;
    for filename in os.listdir(path):
        print("open:" + filename) #print name of the file
        file = open(path + filename,encoding="utf8")

        text = file.read()

        print("tokenize")  # print name of the file
        tokenizedText = tokenizer.tokenize(text)

        words = list()

        for token in tokenizedText :
            words.append(token[1])

        allWords.extend(words)

        print("ngramize")  # print name of the file
        ngramWords = ngramizer.ngramilize(words,3);
        print(ngramWords);

        amountFiles += 1
        if amountFiles >= MAX_FILES :
            break


    frequencyList = frequencies(allWords);
    print(frequencyList.items())






