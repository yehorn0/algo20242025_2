from typing import Callable
from clean_functions import clean_name, clean_name_upper


def hello(name: str, clean_func: Callable[[str], str]) -> None:
    print(f"Hello {clean_func(name)}")


def main() -> None:
    name: str = input("What is your name? ")
    hello(name, clean_name_upper)


if __name__ == "__main__":
    main()
