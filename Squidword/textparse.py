#file for parsing text files, and different types of files to add to the trie
import re

class S_classify:
    @staticmethod
    def issentence(string):
        return bool(re.match(r"^[a-zA-Z1-9 ,;:]+\.$", string))

    @staticmethod
    def isquestion(string):
        return bool(re.match(r"^[a-zA-Z1-9 ,;:]+\?$", string))

    @staticmethod
    def contains_sentence(string):
        return bool(re.search(r"[a-zA-Z1-9 ,;:]+\.", string))

    @staticmethod
    def contains_question(string):
        return bool(re.search(r"[a-zA-Z1-9 ,;:]+\?", string))