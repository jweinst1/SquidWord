#file that implements the cli interface
from Squidword import Sentence_Trie, Trie_Utils

#function that allows the user to interact with, and store data in realtime in a loop
def CLI_run():
    import re
    sbox = Sentence_Trie.strie()
    print("A new language has been created.")
    print("To record a statement, please say PUT, then your sentence.")
    print("If you want to generate a random statement, say RANDOM")
    print("To terminate the program, say EXIT")
    while True:
        response = input()
        if re.match(r"^PUT.*$", response):
            sentence = re.match(r"^PUT (.+)$").group()
            sbox.statement(sentence)
            print("Statement recorded")
        elif response == "RANDOM":
            print(Trie_Utils.random_statement(sbox))
        elif response == "EXIT":
            break
        else:
            print("That command is not recognized")
    pass