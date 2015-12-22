import sys, os
from Squidword import Sentence_Trie, textparse, Trie_Utils, CLI_funcs

#command module for executing the package



def init_squid():
    directory = '.squidword'
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("storage directory initialized")
    else:
        print(".squid directory already exists")

def squid_list():
    return os.listdir(".squidword")

def new_trie(docname, savename):
    current = Sentence_Trie.strie()
    with open(docname, 'r') as target:
        f = target.read()
        statements = textparse.harvestor.getallsentences(f)
        for elem in statements:
            current.statement(elem)
        questions = textparse.harvestor.getallquestions(f)
        for elem in questions:
            current.statement(elem)
        exclamations = textparse.harvestor.getallexclamations(f)
        for elem in exclamations:
            current.statement(elem)
        jsonname = savename + ".json"
        current.savetrie(jsonname)
        print("file scanned and parsed correctly")

def extend_trie(docname, savename):
    jsonname = savename + ".json"
    current = Sentence_Trie.strie(jsonname)
    with open(docname, 'r') as target:
        f = target.read()
        statements = textparse.harvestor.getallsentences(f)
        for elem in statements:
            current.statement(elem)
        questions = textparse.harvestor.getallquestions(f)
        for elem in questions:
            current.statement(elem)
        exclamations = textparse.harvestor.getallexclamations(f)
        for elem in exclamations:
            current.statement(elem)
        current.savetrie(jsonname)
        print("file scanned and parsed correctly")
#gets a link from an html source, and parses the language from it
def get_trie_from_link(link, savename):
    jsonname = savename + ".json"
    link_words = textparse.HTML.getHTMLstr(link)
    link_sents = textparse.HTML.removebrackets(link_words)
    if os.path.exists(os.path.join(".squidword", jsonname)):
        current = Sentence_Trie.strie(jsonname)
        statements = textparse.harvestor.getallsentences(link_sents)
        for elem in statements:
            current.statement(elem)
        questions = textparse.harvestor.getallquestions(link_sents)
        for elem in questions:
            current.statement(elem)
        exclamations = textparse.harvestor.getallexclamations(link_sents)
        for elem in exclamations:
            current.statement(elem)
        current.savetrie(jsonname)
    else:
        current = Sentence_Trie.strie()
        statements = textparse.harvestor.getallsentences(link_sents)
        for elem in statements:
            current.statement(elem)
        questions = textparse.harvestor.getallquestions(link_sents)
        for elem in questions:
            current.statement(elem)
        exclamations = textparse.harvestor.getallexclamations(link_sents)
        for elem in exclamations:
            current.statement(elem)
        current.savetrie(jsonname)


if sys.argv[1] == 'put':
    #first one is file to scan, second one is name of language in .squidword directory
    extend_trie(sys.argv[2], sys.argv[3])
elif sys.argv[1] == 'start':
    #first one is file to scan, second is just the name of language
    new_trie(sys.argv[2], sys.argv[3])

elif sys.argv[1] == 'random':
    jsonname = sys.argv[2] + ".json"
    box = Sentence_Trie.strie(jsonname)
    print(Trie_Utils.random_statement(box))

elif sys.argv[1] == 'files':
    print(squid_list())
elif sys.argv[1] == 'getfile':
    import shutil
    jsonname = sys.argv[2] + ".json"
    dirpath = os.path.join(".squidword", jsonname)
    shutil.copy2(dirpath, jsonname)
    print("file copied successfully")

elif sys.argv[1] == 'init':
    init_squid()
elif sys.argv[1] == 'CLI':
    CLI_funcs.CLI_run()
elif sys.argv[1] == 'link':
    get_trie_from_link(sys.argv[2], sys.argv[3])


