import unittest
from regex_parser import RegexParser
from direct_construction import DirectAFDConstructor
from simulation import simulate_afd

class TestAutomata(unittest.TestCase):
    def test_regex_parser(self):
        self.assertEqual(RegexParser.infix_to_postfix("a|b"), "ab|")
        self.assertEqual(RegexParser.infix_to_postfix("(a.b)*"), "ab.*")

    def test_afd_construction(self):
        regex = "a|b"
        afd = DirectAFDConstructor(RegexParser.infix_to_postfix(regex)).get_afd()
        self.assertIsNotNone(afd)

    def test_simulation(self):
        regex = "a.b"
        afd = DirectAFDConstructor(RegexParser.infix_to_postfix(regex)).get_afd()
        self.assertTrue(simulate_afd(afd, "ab"))
        self.assertFalse(simulate_afd(afd, "a"))

if __name__ == "__main__":
    unittest.main()
