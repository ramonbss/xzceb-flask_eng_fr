import unittest
from translator import english_to_french, french_to_english

class TestMachineTranslation(unittest.TestCase):

    def test_english_to_french(self):
        self.assertIsNotNone(english_to_french('House'),
            'Translation is None')
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_french_to_english(self):
        self.assertIsNotNone(french_to_english('Maison'),
            'Translation is None')
        self.assertEqual(french_to_english('Bonjour'),'Hello')


if __name__ == '__main__':
    unittest.main()