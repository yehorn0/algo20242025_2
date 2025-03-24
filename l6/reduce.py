from typing import Callable, TypeVar
from functools import reduce

T = TypeVar('T')


def reduce_function(func: Callable[[T, T], T], arr: list[T] = None, initial: T | None = None) -> list[T]:
    if initial:
        result = initial
    else:
        result = next(iter(arr))

    for elem in arr:
        result = func(result, elem)

    return result


def double_sum(x: T, y: T) -> T:

    return x + y


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    reduced = 0

    for number in numbers:
        reduced += number

    print(reduced)

    print(reduce_function(double_sum, numbers, 0))

    print(reduce(double_sum, numbers, 0))
