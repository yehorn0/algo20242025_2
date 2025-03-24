from typing import Any, Optional, Callable, Self


def reverse_not_clean(arr: list[Any]) -> None:
    for idx in range(len(arr) // 2):
        arr[idx], arr[len(arr) - idx - 1] = arr[len(arr) - idx - 1], arr[idx]


def reverse(arr: list[Any]) -> list[Any]:
    return arr[::-1]


def some_function_not_clean(arr: list[Any] = []) -> list[Any]:
    arr.append(2)

    return arr


def some_function(arr: Optional[list[Any]] = None) -> list[Any]:
    if not arr:
        arr = []

    arr.append(2)

    return arr


class Maybe:
    def __init__(self, value: Any) -> None:
        self.value = value

    def bind(self, func: Callable) -> Callable | Self:
        if self.value is None:
            return Maybe(None)

        return func(self.value)

    def __repr__(self) -> str:
        return f"Maybe({self.value})"


def div_(x: float, y: float) -> float:
    return x / y


def safe_div(x: float, y: float) -> Maybe:
    return Maybe(None) if y == 0 else Maybe(div_(x, y))


if __name__ == '__main__':
    array_ = [1, 2, 3, 4, 6]

    reversed_array = reverse(array_)

    print(reversed_array)

    tuple_  = (1, 2, 3, 4, 6)

    problem_tuple = (1, 2, [0, 2])
    problem_tuple[2].append(3)
    print(problem_tuple)

    print(some_function_not_clean())
    print(some_function_not_clean())
    print(some_function_not_clean())

    print(some_function())
    print(some_function())
    print(some_function())

    print(safe_div(2, 0))

