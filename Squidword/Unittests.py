import unittest
from Squidword.Sentence_Trie import *
from Squidword import Trie_Utils
from Squidword import __main__



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
    def Insertion_test03(self):
        f = strie()
        f.statement("People don't love corn.")
        f.statement("People do love corn.")
        f.statement("People can love corn.")
        f.statement("People could love corn.")
        self.assertEqual({'People': {'do': {'love': {'corn.': {}}}, 'could': {'love': {'corn.': {}}}, 'can': {'love': {'corn.': {}}}, "don't": {'love': {'corn.': {}}}}}, f.trie)

class random_statements(unittest.TestCase):
   #tests random generation of natural phrases
    def random_test01(self):
        f = strie()
        f.statement("People don't love corn.")
        f.statement("People do love corn.")
        f.statement("People can love corn.")
        f.statement("People could love corn.")
        result = Trie_Utils.random_statement(f)
        self.assertTrue(f.istrue(result))
    def random_test02(self):
        f = strie()
        f.statement("I need lettuce.")
        f.statement("Me and samuel go to the park.")
        f.statement("People can love corn.")
        f.statement("People could love corn.")
        result = Trie_Utils.random_statement(f)
        self.assertTrue(f.istrue(result))

class File_tests(unittest.TestCase):

    def file_test01(self):
        import os
        __main__.init_squid()
        self.assertTrue(os.path.exists(".squidword"))
    def trie_createtest(self):
        import os
        __main__.new_trie("practice.txt", "firstsave")
        self.assertTrue(os.path.exists(os.path.join(".squidword", "firstsave")))
if __name__ == '__main__':
    unittest.main()
