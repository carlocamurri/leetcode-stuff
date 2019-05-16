import unittest

import test.tools.name_converter as converter


class NameConverterTest(unittest.TestCase):

    def test_single_word_name_is_capitalized(self):
        result = converter.convert('name')
        self.assertEqual(result, 'Name')

    def test_multiple_word_name_is_capitalized_correctly(self):
        result = converter.convert('many_words_name')
        self.assertEqual(result, 'ManyWordsName')


if __name__ == '__main__':
    unittest.main()
