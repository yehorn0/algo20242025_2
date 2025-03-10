import unittest


class CalculatorSquareTestCase(unittest.TestCase):
    def setUp(self) -> None:
        from l4.src.square import square, bad_square

        self.tested_func = square

    def tearDown(self):
        ...

    def test_positive_number(self):
        # Arrange
        number = 4
        expected = 16

        # Act
        actual = self.tested_func(number)

        # Assert
        self.assertEqual(actual, expected)

    def test_negative_number(self):
        # Arrange
        number = -3
        expected = 9

        # Act
        actual = self.tested_func(number)

        # Assert
        self.assertEqual(actual, expected)

    def test_zero(self):
        # Arrange
        number = 0
        expected = 0

        # Act
        actual = self.tested_func(number)

        # Assert
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
