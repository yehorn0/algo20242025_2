import math
import matplotlib.pyplot as plt
from typing import Callable


def draw_functions(funcs: list[Callable[[float], float]]) -> None:
    xs = list(range(10, 10000, 100))

    plt.figure(figsize=(10, 6))

    for func in funcs:
        plt.plot(xs, [math.log10(func(x)) for x in xs])

    plt.title("Big-O (small?)")

    plt.show()


def linear(x: float) -> float:
    return x - 1


if __name__ == '__main__':
    functions = [
        lambda x: 2*x - 1,
        linear,
        lambda x: math.log(x) + 4,
        lambda x: x*math.log(x) - 3,
        lambda x: x**2 + 2,
        lambda x: 3*x**2 - 2
    ]

    draw_functions(functions)

    # draw_functions([1])
"""
vector<T> vec...
for (auto &elem :: vec) {

}

"""