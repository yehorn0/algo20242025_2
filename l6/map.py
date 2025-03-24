from typing import Callable, TypeVar

T = TypeVar('T')


def map_function(func: Callable[[T], T], arr: list[T] = None) -> list[T]:
    if not arr:
        arr = []

    return [
        func(elem) for elem in arr
    ]


def linear(x: T) -> T:
    return x ** 2 + 3


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # x^2 + 3
    mapped_numbers = []

    for number in numbers:
        mapped_numbers.append(number ** 2 + 3)

    print(mapped_numbers)

    print(map_function(linear, numbers))

    mapped_numbers_map = map(linear, numbers)
    print(list(mapped_numbers_map))

    mapped_numbers_map_lambda = map(lambda x: x**2 + 3, numbers)
    print(list(mapped_numbers_map_lambda))
