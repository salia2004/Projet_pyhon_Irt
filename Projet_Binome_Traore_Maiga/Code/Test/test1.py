import unittest
from Code.exercice1 import verifier_balises, compter_balises, compter_balises_p, balises_dans_body

class TestExercice1(unittest.TestCase):
    def test_verifier_balises(self):
        html_code_correct = "<html><body><p>Exemple</p></body></html>"
        html_code_incorrect = "<html><body><p>Exemple</body></html>"
        self.assertTrue(verifier_balises(html_code_correct))
        self.assertFalse(verifier_balises(html_code_incorrect))

    def test_compter_balises(self):
        with open("exemple.html", "w") as file:
            file.write("<html><body><p>Test</p><p>Autre Test</p></body></html>")
        result = compter_balises("exemple.html")
        expected_result = {'html': 1, 'body': 1, 'p': 2}
        self.assertEqual(result, expected_result)

    def test_compter_balises_p(self):
        html_code = "<html><body><p>Test</p><p>Exemple</p></body></html>"
        self.assertEqual(compter_balises_p(html_code), 2)

    def test_balises_dans_body(self):
        html_code = "<html><body><p>Test</p><p>Exemple</p></body></html>"
        result = balises_dans_body(html_code)
        expected_result = ['p', 'p']
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
