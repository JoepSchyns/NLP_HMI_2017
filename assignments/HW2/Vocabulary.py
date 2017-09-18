import os
import string
from collections import defaultdict
import SimpleTokenizer

class Vocabulary :
    path = '../../datasets/blogs/train/'

    tokenizer = SimpleTokenizer.SimpleTokenizer()

    allWords = list()

    for filename in os.listdir(path):
        # print(filename) #print name of the file
        file = open(path + filename,encoding="utf8")

        text = file.read()

        tokenizedText = tokenizer.tokenize(text)

        words = list()

        for token in tokenizedText :
            words.append(token[1])

        allWords.extend(words)

    frequencyList = defaultdict(int)
    for item in allWords :
        frequencyList[item] += 1

    print(frequencyList.items())


    def ngramilizer(words,n) : #TODO stop at the stop token
        ngram = list()
        i = 0
        while i < len(words):
            ngram.append(" ".join(words[i:(i + n)])) #get ngram and add to the list
            i += n + 1;

        return ngram



