import unittest
from regex_parser import RegexParser
from direct_construction import DirectAFDConstructor
from simulation import simulate_afd

class TestExtendedAutomata(unittest.TestCase):

    def test_afd_construction_various(self):
        """ Prueba la construcción del AFD con diferentes expresiones regulares """
        regex_cases = ["a*b+", "a(b|c)*d", "0(1|0)*1"]
        for regex in regex_cases:
            with self.subTest(regex=regex):
                afd = DirectAFDConstructor(RegexParser.infix_to_postfix(regex)).get_afd()
                self.assertIsNotNone(afd, f"El AFD para '{regex}' no debe ser None")

    def test_simulation_valid_cases(self):
        """ Prueba que el AFD acepte cadenas válidas en distintas expresiones """
        test_cases = {
            "a*b+": ["ab", "aab", "aaaabb"],
            "a(b|c)*d": ["ad", "abd", "acbd", "abcbcd"],
            "0(1|0)*1": ["01", "001", "011", "0101"]
        }

        for regex, valid_cases in test_cases.items():
            with self.subTest(regex=regex):
                afd = DirectAFDConstructor(RegexParser.infix_to_postfix(regex)).get_afd()
                for case in valid_cases:
                    with self.subTest(case=case):
                        self.assertTrue(simulate_afd(afd, case), f"La cadena '{case}' debería ser aceptada en '{regex}'.")

    def test_simulation_invalid_cases(self):
        """ Prueba que el AFD rechace cadenas inválidas en distintas expresiones """
        test_cases = {
            "a*b+": ["ba", "bb", "abb"],
            "a(b|c)*d": ["d", "bd", "abc"],
            "0(1|0)*1": ["1", "00", "000"]
        }

        for regex, invalid_cases in test_cases.items():
            with self.subTest(regex=regex):
                afd = DirectAFDConstructor(RegexParser.infix_to_postfix(regex)).get_afd()
                for case in invalid_cases:
                    with self.subTest(case=case):
                        self.assertFalse(simulate_afd(afd, case), f"La cadena '{case}' no debería ser aceptada en '{regex}'.")

if __name__ == "__main__":
    unittest.main()
