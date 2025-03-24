from typing import Callable, TypeVar

T = TypeVar('T')


def filter_function(func: Callable[[T], bool], arr: list[T] = None) -> list[T]:
    if not arr:
        arr = []

    return [
        elem for elem in arr if func(elem)
    ]


def is_even(num: int) -> bool:
    return num % 2 == 0


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    print(even_numbers)

    even_numbers = [number for number in numbers if number % 2 == 0]
    print(even_numbers)

    print(filter_function(is_even, even_numbers))

    even_numbers_filter = filter(is_even, even_numbers)

    print(list(even_numbers_filter))

    even_numbers_filter_lambda = filter(lambda x: x % 2 == 0, even_numbers)
    print(list(even_numbers_filter_lambda))
