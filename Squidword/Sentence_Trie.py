#Sentence trie object, that binds phrases into tries, for easy look up and storage
import json

class strie (object):

    def __init__(self, wordfile=None):
        if wordfile:
            with open(wordfile, 'r') as wordbase:
                words = json.loads(wordbase.read())
                self.trie = words
        else:
            self.trie = {}
    def __repr__(self):
        return str(self.trie)
    def __str__(self):
        return str(self.trie)
    def statement(self, phrase):
        phrase = phrase.lower()
        words = phrase.split()
        current = self.trie
        while len(words) > 0:
            word = words.pop(0)
            if word in current.keys():
                current = current[word]
            else:
                current[word] = {}
                current = current[word]
    def istrue(self, phrase):
        phrase = phrase.lower()
        words = phrase.split()
        current = self.trie
        while len(words) > 0:
            word = words.pop(0)
            if word in current.keys():
                current = current[word]
            else:
                return False
        return True
    def savetrie(self, docname):
        word_data = json.dumps(self.trie)
        with open(docname, 'w') as wordbase:
            wordbase.write(word_data)
            wordbase.close()
            return "Text is Stored"
    def processstring(self, string):
        return string.lower()