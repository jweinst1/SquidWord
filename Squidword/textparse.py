#file for parsing text files, and different types of files to add to the trie
import re

class S_classify:
    @staticmethod
    def issentence(string):
        return bool(re.match(r"^[a-zA-Z1-9 ,;':]+\.$", string))

    @staticmethod
    def iswordseq(string):
        return bool(re.match(r"^[a-zA-Z]+ [a-zA-Z]*$"))

    @staticmethod
    def isquestion(string):
        return bool(re.match(r"^[a-zA-Z1-9 ,;':]+\?$", string))

    @staticmethod
    def isexclamation(string):
        return bool(re.match(r"^[a-zA-Z1-9 ,;':]+\!$", string))

    @staticmethod
    def contains_sentence(string):
        return bool(re.search(r"[a-zA-Z1-9 ,;':]+\.", string))

    @staticmethod
    def contains_question(string):
        return bool(re.search(r"[a-zA-Z1-9 ,;':]+\?", string))

    @staticmethod
    def contains_exclamation(string):
        return bool(re.search(r"[a-zA-Z1-9 ,;':]+\!", string))

class deletor:
#class for deleting unwanted symbols
    @staticmethod
    def remove_sym(string):
        return re.sub(r"[\@\#\$%\^\&\*\(\)\{\}\+\=\<\>\~]", "", string)
    #removes all non alpha numeric characters
    @staticmethod
    def only_words(string):
        return re.sub(r"[^a-zA-Z1-9 ]", "", string)

    @staticmethod
    def remove_word(string, word):
        word = " " + word + " "
        return re.sub(word, "", string)

    #removes multiple words from a text
    @staticmethod
    def remove_words(string, words):
        for elem in words:
            elem = " " + elem + " "
            string = re.sub(elem, "", string)
        return string

    @staticmethod
    def remove_spaces(string):
        return re.sub(r" ", "", string)
#removes all content between brackets
    @staticmethod
    def remove_brackets(string):
        return re.sub(r"\([^\(\)]\)", "", string)

class harvestor:

    @staticmethod
    def getallsentences(string):
        return re.findall(r"[a-zA-Z1-9,;':]+ [a-zA-Z1-9, ;':]+\.", string)

    @staticmethod
    def getallquestions(string):
        return re.findall(r"[a-zA-Z1-9,;':]+ [a-zA-Z1-9, ;':]+\?", string)

    @staticmethod
    def getallexclamations(string):
        return re.findall(r"[a-zA-Z1-9,;':]+ [a-zA-Z1-9, ;':]+\!", string)

class HTML:
#class for implementing harvesting for HTML documents and links

    @staticmethod
    def getHTMLstr(link):
        import urllib.request
        with urllib.request.urlopen(link) as sitetext:
            strform = sitetext.read()
            strform = strform.decode("utf-8")
            return strform

    @staticmethod
    def removebrackets(string):
        return re.sub(r"<[^<>]>", "", string)
