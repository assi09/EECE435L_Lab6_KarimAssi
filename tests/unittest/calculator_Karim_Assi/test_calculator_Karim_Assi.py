import sys
import unittest
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parents[3] / "src" / "main" / "python"
sys.path.insert(0, str(SOURCE_ROOT))

from calculator_Karim_Assi import (  # noqa: E402
    add,
    divide,
    modulus,
    multiply,
    power,
    square_root,
    subtract,
)


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-2, 5), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 4), -3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-3, 4), -12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(1, 2), 0.5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(12, 4), 0)
        with self.assertRaises(ValueError):
            modulus(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertAlmostEqual(power(4, 0.5), 2)

    def test_square_root(self):
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
