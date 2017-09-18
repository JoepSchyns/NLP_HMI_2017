import os
import glob
import SimpleTokenizer

class Vocabulary :
    path = '../../datasets/blogs/train/'

    tokenizer = SimpleTokenizer.SimpleTokenizer()

    for filename in os.listdir(path):
        print(filename)
        file = open(path + filename,encoding="utf8")

        text = file.read()

        print(tokenizer.tokenize(text))


