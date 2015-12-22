import unittest
from Squidword.Sentence_Trie import *



class Trie_tests(unittest.TestCase):
    #tests that investigate the utility of the sentence trie object
    def Insertion_test01(self):
        box = strie()
        box.statement("i love apples")
        self.assertEqual({'i': {'love': {'apples': {}}}}, box.trie)
    def Insertion_test02(self):
        box = strie()
        box.statement("i love corn.")
        box.statement("i love chicken.")
        self.assertEqual({'i': {'love': {'chicken.': {}, 'corn.': {}}}}, box.trie)


if __name__ == '__main__':
    unittest.main()
