"""
This file contains solutions for the Two Sum problem.
"""


def two_sum_optimal(nums: list[int], target: int) -> list[int] | None:
    """
    Finds two numbers in a list that add up to a target value using a hash map.

    This is the optimal solution with O(n) time complexity.

    Args:
        nums: A list of integers.
        target: The target integer sum.

    Returns:
        A list containing the indices of the two numbers, or None if no solution is found.
    """
    seen_numbers = {}  # Dictionary to store number -> index
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen_numbers:
            return [seen_numbers[difference], i]
        seen_numbers[num] = i
    return None  # Or raise an error, as problem statement guarantees a solution.


def two_sum_brute_force(nums: list[int], target: int) -> list[int] | None:
    """
    Finds two numbers in a list that add up to a target value using nested loops.

    This is the brute-force solution with O(n^2) time complexity.

    Args:
        nums: A list of integers.
        target: The target integer sum.

    Returns:
        A list containing the indices of the two numbers, or None if no solution is found.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# --- Tests ---
if __name__ == "__main__":
    # Test cases
    test1_nums, test1_target = [2, 7, 11, 15], 9
    test2_nums, test2_target = [3, 2, 4], 6
    test3_nums, test3_target = [3, 3], 6

    # Optimal solution
    assert sorted(two_sum_optimal(test1_nums, test1_target)) == [0, 1]
    assert sorted(two_sum_optimal(test2_nums, test2_target)) == [1, 2]
    assert sorted(two_sum_optimal(test3_nums, test3_target)) == [0, 1]

    # Brute-force solution
    assert sorted(two_sum_brute_force(test1_nums, test1_target)) == [0, 1]
    assert sorted(two_sum_brute_force(test2_nums, test2_target)) == [1, 2]
    assert sorted(two_sum_brute_force(test3_nums, test3_target)) == [0, 1]

    print("All tests passed!")
