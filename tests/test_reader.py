import unittest
from reader import *
from glc import Grammar 

class TestReader(unittest.TestCase):
    def setUp(self):
        print('Running ' + self._testMethodName)

    """
    def test_read_glc(self):
        a = Grammar("S -> aS | bB \n B -> cS | f"))
        self.assertTrue(a.accepts('aaaaabcaaaabf'))
        self.assertTrue(a.accepts('bf'))
        self.assertTrue(a.accepts('bcaaaabf'))
        self.assertTrue(a.accepts('abcabcabcabf'))
        self.assertFalse(a.accepts('bcf'))
        self.assertFalse(a.accepts('aaaacf'))
        self.assertFalse(a.accepts(''))

        a = Grammar("S -> a | cB | & \n B -> f"))
        self.assertTrue(a.accepts('a'))
        self.assertTrue(a.accepts('cf'))
        self.assertTrue(a.accepts(''))
        self.assertFalse(a.accepts('c'))
        self.assertFalse(a.accepts('f'))
        self.assertFalse(a.accepts('acf'))
        
        a = Grammar("S -> a \n S -> cB | & \n B -> f"))
        self.assertTrue(a.accepts('a'))
        self.assertTrue(a.accepts('cf'))
        self.assertTrue(a.accepts(''))
        self.assertFalse(a.accepts('c'))
        self.assertFalse(a.accepts('f'))
        self.assertFalse(a.accepts('acf'))

        a = Grammar("Start -> fZ \n Z -> zZ | yZ | z"))
        self.assertTrue(a.accepts('fyz'))
        self.assertTrue(a.accepts('fz'))
        self.assertTrue(a.accepts('fzzyyzz'))
        self.assertFalse(a.accepts('z'))
        self.assertFalse(a.accepts('fzzzy'))
        self.assertFalse(a.accepts(''))
    """

    def test_read_glc_error(self):
        with self.assertRaises(SyntaxError):
            a = Grammar("")
        with self.assertRaises(SyntaxError):
            a = Grammar("S")
        with self.assertRaises(SyntaxError):
            a = Grammar("SA")
        with self.assertRaises(SyntaxError):
            a = Grammar("S1E")
        with self.assertRaises(SyntaxError):
            a = Grammar("S -> aS | a |")
        with self.assertRaises(SyntaxError):
            a = Grammar("B -> aA \n S -> aS | | a")
        with self.assertRaises(SyntaxError):
            a = Grammar("S aA | a")
        with self.assertRaises(SyntaxError):
            a = Grammar("s -> aA | a")
        with self.assertRaises(SyntaxError):
            a = Grammar("S -> aA | a \n A -> a | a&")


if __name__ == "__main__":
    unittest.main()