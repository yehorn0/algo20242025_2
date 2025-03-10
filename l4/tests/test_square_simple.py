from typing import Callable
from l4.src.square import square, bad_square


def test_parametrized(
        tested_func: Callable[[int], int],
        params: list[tuple[int, int]]
) -> tuple[int, int]:
    failed_count = passed_count = 0
    for in_value, out_value in params:
        actual_value = tested_func(in_value)
        try:
            assert actual_value == out_value
            passed_count += 1
        except AssertionError:
            failed_count += 1
            print(f"{tested_func.__name__} failed for in data: {in_value}. "
                  f"Expected: {out_value}. Actual: {actual_value}")

    return failed_count, passed_count


def test_square() -> None:
    # if square(2) != 4:
    #     print("2 square is not equal to 4")
    #
    # if square(6) != 36:
    #     print("6 square is not equal to 36")
    # failed_count = passed_count = 0
    # try:
    #     assert square(2) == 4
    #     passed_count += 1
    # except AssertionError:
    #     failed_count += 1
    #     print("2 square is not equal to 4")
    #
    # try:
    #     assert square(6) == 36, "6 square is not equal to 36"
    #     passed_count += 1
    # except AssertionError:
    #     failed_count += 1
    #     print("6 square is not equal to 36")
    #
    # try:
    #     assert square(0) == 0, "0 square is not equal to 0"
    #     passed_count += 1
    # except AssertionError:
    #     failed_count += 1
    #     print("0 square is not equal to 0")

    test_data = [
        (2, 4),
        (7, 49),
        (0, 0)
    ]

    #failed_count, passed_count = test_parametrized(square, test_data)
    failed_count, passed_count = test_parametrized(bad_square, test_data)

    if failed_count == 0:
        print("All tests passed")
    else:
        print(f"Passed tests: {passed_count}. Failed tests: {failed_count}. "
              f"Total: {passed_count + failed_count}")


if __name__ == '__main__':
    test_square()
