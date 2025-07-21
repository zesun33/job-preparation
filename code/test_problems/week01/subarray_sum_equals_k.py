from typing import List

"""
Subarray Sum Equals K (from LeetCode)
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""


# Optimal Solution: Prefix Sum with Hash Map
# Time: O(n)
# Space: O(n)
def subarray_sum_prefix_sum(nums: List[int], k: int) -> int:
    """
    Finds the total number of continuous subarrays whose sum equals k using a hash map.

    This optimal approach uses the concept of prefix sums to find the total
    count in a single pass. A prefix sum is the sum of all elements from the
    start of the array up to a given index.

    The key insight is: if the cumulative sum up to two indices (say, i and j)
    is the same, then the sum of the elements between those indices is zero.
    Extending this, if `sum(0, j) - sum(0, i) = k`, then the subarray `(i, j]`
    sums to `k`. We can rearrange this to `sum(0, i) = sum(0, j) - k`.

    So, as we iterate through the array calculating the `current_sum` (our `sum(0, j)`),
    we just need to check if `current_sum - k` exists in our hash map of
    previously seen prefix sums (`sum(0, i)`).

    Args:
        nums: A list of integers.
        k: The target integer sum.

    Returns:
        The total number of continuous subarrays summing to k.
    """
    count = 0
    current_sum = 0
    # The map stores {prefix_sum: frequency}. We initialize with {0: 1} to handle
    # cases where a subarray starts from the beginning of the array.
    prefix_sum_map = {0: 1}

    for num in nums:
        current_sum += num
        # Check if a subarray exists that sums to k
        if current_sum - k in prefix_sum_map:
            count += prefix_sum_map[current_sum - k]

        # Add the current prefix sum to the map, or increment its count
        prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1

    return count


# Alternative Solution: Brute Force
# Time: O(n^2)
# Space: O(1)
def subarray_sum_brute_force(nums: List[int], k: int) -> int:
    """
    Finds the total number of subarrays summing to k using nested loops.

    This straightforward approach checks every possible continuous subarray.
    It iterates through all possible start points and, for each start point,
    iterates through all possible end points, calculating the sum along the way.

    While easy to understand, it's too slow for large inputs.
    """
    count = 0
    n = len(nums)
    for i in range(n):
        running_sum = 0
        for j in range(i, n):
            running_sum += nums[j]
            if running_sum == k:
                count += 1
    return count


# --- Tests ---
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
        ([1], 1, 1),
        ([1], 0, 0),
        ([], 5, 0),
    ]

    for nums, k, expected in test_cases:
        # Test optimal solution
        result_optimal = subarray_sum_prefix_sum(nums, k)
        assert (
            result_optimal == expected
        ), f"Optimal failed on {nums}, {k}: got {result_optimal}, want {expected}"

        # Test brute-force solution
        result_brute = subarray_sum_brute_force(nums, k)
        assert (
            result_brute == expected
        ), f"Brute-force failed on {nums}, {k}: got {result_brute}, want {expected}"

    print("All tests passed!")
