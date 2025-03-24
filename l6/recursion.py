import sys


def print_by_char(msg: str) -> None:
    try:
        print(msg[0], end="")
    except IndexError:
        print()
        return

    print_by_char(msg[1:])

# N! = N * (N-1) * (N-2) * ... * 2 * 1
# 0! = 1


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(5))
