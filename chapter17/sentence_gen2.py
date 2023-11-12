#

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence2:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

    def __repr__(self):
        return f'fSentence({reprlib.repr(self.text)})'
