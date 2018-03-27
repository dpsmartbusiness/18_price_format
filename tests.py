import unittest
from format_price import format_price


class TestPriceFormat(unittest.TestCase):
    def test_format_float(self):
        price = format_price(50.123123)
        self.assertEqual(price, '50.12')

    def test_format_float_negative(self):
        price = format_price(-134.1523213)
        self.assertEqual(price, '-134.15')

    def test_format_integer(self):
        price = format_price(20)
        self.assertEqual(price, '20')

    def test_format_integer_negative(self):
        price = format_price(-100)
        self.assertEqual(price, '-100')

    def test_format_integer_with_zeros(self):
        price = format_price(72.0000000)
        self.assertEqual(price, '72')

    def test_format_integer_negative_with_zeros(self):
        price = format_price(-55.0000)
        self.assertEqual(price, '-55')

    def test_format_zero(self):
        price = format_price(0)
        self.assertEqual(price, '0')

    def test_format_letters(self):
        price = format_price('asdasd')
        self.assertIsNone(price)

    def test_format_none(self):
        price = format_price(None)
        self.assertIsNone(price)

    def test_format_list(self):
        price = format_price([(20, 12, 100)])
        self.assertIsNone(price)

    def test_format_float_rounding(self):
        price = format_price(33.6999)
        self.assertEqual(price, '33.70')

    def test_format_integer_part(self):
        price = format_price(3500.12)
        self.assertEqual(price, '3 500.12')

if __name__ == '__main__':
    unittest.main()