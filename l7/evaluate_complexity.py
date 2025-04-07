import math
import time
import random
from typing import Callable
import matplotlib.pyplot as plt

from l7.locate_element import locate_element_linear, locate_element as locate_element_log


def measure_time(func: Callable[[list[int], int], int], *args) -> float:
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start


def evaluate_complexity(max_n: int = 1_000_000, step: int = 1_000) -> list[tuple[int, float, float]]:
    res = []

    for n in range(0, max_n+1, step):
        data, query = prepare_data(n)
        res.append((
            n,
            measure_time(locate_element_linear, data, query),
            measure_time(locate_element_log, data, query),
        ))

    return res


def prepare_data(n: int) -> tuple[list[int], int]:
    return sorted(
        random.randint(-1000, 1000) for _ in range(n)
    ), random.randint(-1000, 1000)


def plot_complexity(
    data: list[tuple[int, float, float]]
) -> None:
    n = [d[0] for d in data]
    time_linear = [math.log10(d[1]) for d in data]
    time_log = [math.log10(d[2]) for d in data]

    plt.figure(figsize=(8, 8))

    plt.plot(n, time_linear, label="Linear")
    plt.plot(n, time_log, label="Log")

    plt.show()


if __name__ == '__main__':
    plot_complexity(
        evaluate_complexity(100_000, 1000)
    )
