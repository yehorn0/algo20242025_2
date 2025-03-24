from typing import Callable


def outer_function(x: int) -> Callable[[int], int]:
    def inner_function(y: int) -> int:
        return x + y

    return inner_function


add_five = outer_function(5)


def decorator_function(original_function: Callable[[], None]) -> Callable[[], None]:
    def inner_function(*args, **kwargs) -> None:
        print("Inside decorator_function")
        original_function(*args, **kwargs)
        print("After execution")

    return inner_function


@decorator_function
def print_function(str_: str) -> None:
    print(f"Inside some function {str_}")


print_function("some string")

# decorator_function(print_function)()

