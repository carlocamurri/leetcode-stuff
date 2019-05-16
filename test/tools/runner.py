import os
import glob
import importlib
import unittest

import test.tools.parser as parser
import test.tools.expectations_generator as expectations_generator
from test.tools.generator import TestCaseGenerator


os.chdir(os.path.dirname(os.path.realpath(__file__)))


TEST_FOLDER = './..'
SOURCE_FOLDER = './../../src'

TEST_PATH = os.path.abspath(TEST_FOLDER)
SRC_PATH = os.path.abspath(SOURCE_FOLDER)


def run():
    os.chdir(TEST_PATH)
    test_files = glob.glob('*.test')
    os.chdir(SRC_PATH)
    src_files = glob.glob('*.py')
    function_names = [file.split('.')[0] for file in src_files]
    for test_file in test_files:
        func_name = test_file.split('.')[0]
        if func_name in function_names:
            run_test(func_name)


def run_test(func_name):
    module = importlib.import_module('src.' + func_name)
    soln_class = module.Solution
    os.chdir(TEST_PATH)
    filename = func_name + '.test'
    test_text = parser.parse(filename)
    expectations = expectations_generator.generate_expectations(test_text)
    test_class_generator = TestCaseGenerator(soln_class, func_name)
    for expectation in expectations:
        test_class_generator.add_test(expectation[0], expectation[1])
    test_cases = test_class_generator.build_test_cases()
    suite = unittest.TestSuite()
    suite.addTests(test_cases)
    result = unittest.TestResult()
    suite.run(result)
    print(func_name)
    print('\tTests run: {}'.format(result.testsRun))
    for failure in result.failures:
        print('\tFailure of {0}: {1}'.format(failure[0].id(), failure[1]))
    for error in result.errors:
        print('\tError in {0}: {1}'.format(error[0].id(), error[1]))


if __name__ == '__main__':
    run()
