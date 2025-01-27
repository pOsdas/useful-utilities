import unittest

from utils import camel_case_to_snake_case


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass


class Test(BaseTest):
    def test_case_converter(self):
        test_1 = camel_case_to_snake_case("SomeText")
        self.assertEqual(test_1, "some_text")
        test_2 = camel_case_to_snake_case("RSomeText")
        self.assertEqual(test_2, "r_some_text")
        test_3 = camel_case_to_snake_case("SText")
        self.assertEqual(test_3, "s_text")


