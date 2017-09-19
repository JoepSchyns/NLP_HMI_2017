import re
import string

class SimpleTokenizer :

    START_TOKEN = "START"
    STOP_TOKEN = "STOP"

    def __init__(self):
        self.scanner = re.Scanner([
          (r"[0-9]+",lambda scanner,token:("INTEGER", token)),
          (r"[a-z_]+",lambda scanner,token:("IDENTIFIER", token)),
         (r"[A-Z_]+", lambda scanner, token: ("IDENTIFIER", token)),
          (r"[,.'\";:<>?]+",lambda scanner,token:("PUNCTUATION", token)),
          (r"\s+", None), # None == skip token.
        ])


    def tokenize(self,input):
        input = input.lower()

        for c in string.punctuation:
            if (c == '.'):
                input = input.replace(c, self.STOP_TOKEN + " "  + self.START_TOKEN)
            else:
                input = input.replace(c, "")

        result,remainder = self.scanner.scan(input)
        return result

