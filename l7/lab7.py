def count_rotations(nums: list[int]) -> int:
    """
    test_cases = [
        # Standard test case: rotated list with rotation > 0
        ([15, 18, 2, 3, 6, 12], 2),  # Minimum element at index 2, so 2 rotations

        # Case with no rotation (sorted list)
        ([1, 2, 3, 4, 5, 6, 7], 0),  # No rotation, so 0 rotations

        # List rotated only once
        ([7, 1, 2, 3, 4, 5, 6], 1),  # Minimum element at index 1, so 1 rotation

        # List rotated multiple times
        ([4, 5, 6, 7, 1, 2, 3], 4),  # Minimum element at index 4, so 4 rotations

        # List with duplicate elements
        ([10, 10, 10, 1, 10, 10], 3),  # Minimum element at index 3, so 3 rotations

        # Edge case 1: List with a single element
        ([1], 0),  # Only one element, so 0 rotations

        # Edge case 2: List with two elements (rotated)
        ([2, 1], 1)  # Minimum element at index 1, so 1 rotation
    ]
    time complexity = O(log(n)) where n is the length of nums

    :param nums:
    :return:
    """
    ...
