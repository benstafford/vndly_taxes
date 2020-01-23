import unittest

from scanner import Scanner

class TestScanner(unittest.TestCase):
    def test_line_parser(self):
        parsed_result = Scanner.scan(["1 book at 12.49"])
        expected = [{"quantity": "1", "item": "book", "price": "12.49"}]
        self.assertEqual(expected, parsed_result)