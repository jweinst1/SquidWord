#utilities for implementing the word tries

#selects random item from dictionary
def select_rand_item(dict):
    import random
    return random.choice(list(dict.keys()))

#bool function for checking if word terminates a statement
def isterminal(word):
    return word[len(word)-1] == '.' or word[len(word)-1] == '?' or word[len(word)-1] == '!'

#gets a random statement from a trie
def random_statement(trie):
    statement = ""
    current = trie
    while current != {}:
        word = select_rand_item(current)
        if isterminal(word):
            statement += word
            break
        else:
            statement += word + " "
            current = current[word]
    return statement





class wordstack:
    pass