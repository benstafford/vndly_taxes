import unittest

from store import Store

class TestStore(unittest.TestCase):
    def test_receipt_exempt_output(self):
        store = Store([{'quantity': '1', 'item': 'book', 'price': '12.49'}])
        expected = "1 book: 12.49\nSales Taxes: 0.00\nTotal: 12.49"
        self.assertEqual(expected, store.print_receipt())

    def test_receipt_nonexempt_output(self):
        store = Store([{'quantity': '1', 'item': 'music CD', 'price': '14.99'}])
        expected = "1 music CD: 16.49\nSales Taxes: 1.50\nTotal: 16.49"
        self.assertEqual(expected, store.print_receipt())

    def test_receipt_imported_exempt(self):
        store = Store([{'quantity': '1', 'item': 'imported box of chocolates', 'price': '10.00'}])
        expected = "1 imported box of chocolates: 10.50\nSales Taxes: 0.50\nTotal: 10.50"
        self.assertEqual(expected, store.print_receipt())

    def test_receipt_imported_nonexempt(self):
        store = Store([{'quantity': '1', 'item': 'imported bottle of perfume', 'price': '47.50'}])
        expected = "1 imported bottle of perfume: 54.65\nSales Taxes: 7.15\nTotal: 54.65"
        self.assertEqual(expected, store.print_receipt())