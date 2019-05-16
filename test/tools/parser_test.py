import unittest
import os

import test.tools.parser as parser


TEST_FILE_CONTENTS = ['A String\n', 'Another string\n', '\n', 'Yet another \'\' string\n', 'more string']


class ParserTest(unittest.TestCase):

    def test_file_is_parsed_correctly(self):
        contents = parser.parse(os.path.abspath('./parser_test.test'))
        self.assertListEqual(contents, TEST_FILE_CONTENTS)


if __name__ == '__main__':
    unittest.main()