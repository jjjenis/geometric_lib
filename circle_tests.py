import math
from circle import area
from circle import perimeter
import unittest


class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(6)
        self.assertEqual(res, 113.09733552923255)

    def test_area_negative(self):
        res = area(-10)
        self.assertEqual(res, "Error")

    def test_area_real(self):
        res = area(4.5)
        self.assertEqual(res, 63.61725123519331)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = perimeter(6)
        self.assertEqual(res, 37.69911184307752)

    def test_perimeter_negative(self):
        res = perimeter(-10)
        self.assertEqual(res, "Error")

    def test_perimeter_real(self):
        res = perimeter(4.5)
        self.assertEqual(res, 28.274333882308138)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
