import unittest
from typing import Callable


class CalculatorSquareTestCase(unittest.TestCase):
    def setUp(self) -> None:
        from l4.src.lab2 import weights_equilibrium

        self.tested_func: Callable[[list[int]], int] = weights_equilibrium

    def test_empty_list(self):
        # Arrange
        initial_weights = []
        expected_equilibrium = -1

        # Act
        actual_equilibrium = self.tested_func(initial_weights)

        # Assert
        self.assertEqual(actual_equilibrium, expected_equilibrium)

    def test_no_equilibrium_6_6_9(self):
        # Arrange
        initial_weights = [6, 6, 9]
        expected_equilibrium = -1

        # Act
        actual_equilibrium = self.tested_func(initial_weights)

        # Assert
        self.assertEqual(actual_equilibrium, expected_equilibrium)

    def test_equilibrium_43_51_35_4(self):
        # Arrange
        initial_weights = [43, 51, 35, 4]
        expected_equilibrium = 1

        # Act
        actual_equilibrium = self.tested_func(initial_weights)

        # Assert
        self.assertEqual(actual_equilibrium, expected_equilibrium)

    def test_equilibrium_big_list(self):
        # Arrange
        initial_weights = [19, 25, 5, 42, 38, 8, 34, 16, 14, 8, 47, 42, 4, 20, 23]
        expected_equilibrium = 7

        # Act
        actual_equilibrium = self.tested_func(initial_weights)

        # Assert
        self.assertEqual(actual_equilibrium, expected_equilibrium)

    def test_equilibrium_7_24_3_38(self):
        # Arrange
        initial_weights = [7, 24, 3, 38]
        expected_equilibrium = 2

        # Act
        actual_equilibrium = self.tested_func(initial_weights)

        # Assert
        self.assertEqual(actual_equilibrium, expected_equilibrium)


# python -m l4.tests.test_lab2
if __name__ == '__main__':
    unittest.main(verbosity=2)
