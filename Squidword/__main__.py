import sys, os
from Squidword import Sentence_Trie
from Squidword import textparse
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

if sys.argv[1] == 'put':
    pass
elif sys.argv[1] == 'start':
    new_trie(sys.argv[2], sys.argv[3])
elif sys.argv[1] == 'random':
    pass
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
elif sys.argv[1] == 'statement':
    pass
elif sys.argv[1] == 'link':
    pass