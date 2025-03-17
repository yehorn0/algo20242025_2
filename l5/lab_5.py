from typing import Self


class Complex:
    def __init__(self, _re: float = 0., _im: float = 0.) -> None:
        self.__re = _re
        self.__im = _im

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}*i"

    @property
    def real(self) -> float:
        return self.__re

    @real.setter
    def real(self, val: float) -> None:
        self.__re = val

    # Same for properties for imaginary part
    @property
    def imaginary(self) -> float:
        return self.__im

    @imaginary.setter
    def imaginary(self, val: float) -> None:
        self.__im = val

    # Dunder methods
    def __add__(self, other: Self) -> Self: # c1 + c2
        return Complex(self.__re + other.real, self.__im + other.imaginary)

    def __iadd__(self, other: Self) -> Self: # c1 += c2
        self.__re += other.real
        self.__im += other.imaginary

        return self

    def __sub__(self, other: Self) -> Self: # c1 - c2
        ...

    def __mul__(self, other: Self) -> Self: # c1 * c2
        ...

    def __truediv__(self, other: Self) -> Self:  # c1 / c2
        ...

    def __abs__(self) -> Self:
        """
        (a + ib)(a - ib) = a^2 - (ib)^2 = a^2 - i^2*b*2 = a^2 + b^2
        |a + ib| = sqrt(a^2 + b^2)
        """
        ...

    def __eq__(self, other: Self) -> bool: # c1 == c2
        """real == real and imaginary == imaginary
        """
        ...

    def __ne__(self, other: Self) -> bool: # c1 != c2
        """NOT EQUAL :)"""
        ...


if __name__ == "__main__":
    "Re + i*Im"
    c1 = Complex(1., 2.)
    c2 = Complex(2., 3.)
    c3 = c1 + c2
    c1 += c2
    print(c3)
    print(c1)
    #c1 = c1 + 5.
    #print(c1)

"""100
K/P 10
Ispit 40
12 lab po 4
Vstupnij control 2
"""