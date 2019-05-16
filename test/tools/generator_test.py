import unittest

from test.tools.generator import TestCaseGenerator


class Solution:

    def is_even(self, number):
        return number % 2 == 0


if __name__ == '__main__':
    generator = TestCaseGenerator(Solution, 'is_even')
    generator.add_test(2, True)
    generator.add_test(3, False)
    generator.add_test(4, True)
    generator.add_test(5, False)
    generator.add_test(6, False)
    test_cases = generator.build_test_cases()
    suite = unittest.TestSuite()
    suite.addTests(test_cases)
    result = unittest.TestResult()
    suite.run(result)
    assert(len(result.failures) == 1)
    assert(result.testsRun == 5)
    print('Test passed')
