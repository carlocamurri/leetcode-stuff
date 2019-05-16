import unittest
import test.tools.name_converter as converter


class TestCaseGenerator:

    def __init__(self, soln_class, method_name):
        self.soln_class = soln_class
        self.method_name = method_name
        self.test_case = create_test_class(method_name)
        self.test_suffix = 0
        self.test_names = []

    def add_test(self, arguments, expected):
        test = generate_test(self.soln_class, self.method_name, arguments, expected)
        new_test_name = 'test_{}'.format(self.test_suffix)
        setattr(self.test_case, new_test_name, test)
        self.test_names.append(new_test_name)
        self.test_suffix += 1

    def build_test_cases(self):
        return [self.test_case(test_name) for test_name in self.test_names]


def convert_function_name(func):
    def wrapper(name, *args, **kwargs):
        converted_function_name = converter.convert(name)
        return func(converted_function_name, *args, **kwargs)
    return wrapper


@convert_function_name
def create_test_class(name):
    return type(name, (unittest.TestCase, ), {})


def generate_test(soln_class, method_name, arguments, expected):
    def test(self):
        soln = soln_class()
        if isinstance(arguments, tuple):
            result = getattr(soln, method_name)(*arguments)
        else:
            result = getattr(soln, method_name)(arguments)
        self.assertEqual(result, expected)
    return test

