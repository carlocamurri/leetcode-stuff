import unittest

import test.tools.expectations_generator as generator

PRE_IN_1 = '\'String\'\n'
PRE_OUT_1 = 'True\n'

POST_IN_1 = 'String'
POST_OUT_1 = True

SEPARATOR = '\n'

PRE_IN_2 = '[1, 2, 3, 4]\n'
PRE_OUT_2 = '8\n'

POST_IN_2 = [1, 2, 3, 4]
POST_OUT_2 = 8


class ExpectationsGeneratorTest(unittest.TestCase):

    def test_empty_input_generates_no_expectations(self):
        result = generator.generate_expectations([])
        self.assertListEqual(result, [])

    def test_two_consequent_lines_generate_an_expectation(self):
        result = generator.generate_expectations([PRE_IN_1, PRE_OUT_1])
        self.assertListEqual(result, [(POST_IN_1, POST_OUT_1)])

    def test_multiple_expectations_are_generated(self):
        result = generator.generate_expectations([PRE_IN_1, PRE_OUT_1, SEPARATOR, PRE_IN_2, PRE_OUT_2])
        self.assertListEqual(result, [(POST_IN_1, POST_OUT_1), (POST_IN_2, POST_OUT_2)])


if __name__ == '__main__':
    unittest.main()