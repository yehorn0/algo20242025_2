def locate_element_linear(
        numbers: list[int],
        query: int
) -> int:  # time ~ O(n)
    for idx, card in enumerate(numbers):
        if query == card:
            return idx

    return -1


def locate_element(
        numbers: list[int],
        query: int
) -> int:  # time ~ O(logn)
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = numbers[mid]

        if mid_element == query:
            if mid >= 1 and numbers[mid - 1] == mid_element:
                right = mid - 1
            else:
                return mid
        elif mid_element > query:
            left = mid + 1
        else:
            right = mid - 1
    return -1
