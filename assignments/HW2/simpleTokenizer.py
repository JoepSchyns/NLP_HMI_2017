import re
import string

class SimpleTokenizer :
    def __init__(self):
        self.scanner = re.Scanner([
          (r"[0-9]+",lambda scanner,token:("INTEGER", token)),
          (r"[a-z_]+",lambda scanner,token:("IDENTIFIER", token)),
          (r"[,.'\";:<>?]+",lambda scanner,token:("PUNCTUATION", token)),
          (r"\s+", None), # None == skip token.
        ])
        self.startStopScanner = re.Scanner([
            (r"[.?!", lambda scanner, token: ("START_STOP", "STOP START")),
        ])


    def tokenize(self,str):
        str = str.lower()

        #TODO add start and stop

        resultSS, remainderSS = self.startStopScanner.scan(str);

        for c in string.punctuation:
            str = str.replace(c, "")

        result,remainder = self.scanner.scan(str)
        return result;

