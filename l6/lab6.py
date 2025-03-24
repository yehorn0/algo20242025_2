from typing import Callable


def cached(func: Callable[[int], int]) -> Callable[[int], int]:
    ...


@cached
def fibonacci(n: int) -> int:
    ...


# 1 1 2 3 5 8 13 21 34
