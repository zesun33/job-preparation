"""Contains Duplicate - NeetCode 150 #1

Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.

LeetCode Link: https://leetcode.com/problems/contains-duplicate/
"""

from typing import List


# Optimal Solution: Hash Set
# Time: O(n), Space: O(n)
def contains_duplicate(nums: List[int]) -> bool:
    """
    Checks for duplicates using a hash set for efficient O(1) lookups.

    This is the best-balanced solution for most cases. It offers the fastest
    runtime by trading extra space to store seen elements.
    """
    seen = set()
    for n in nums:
        if n in seen:
            return True  # Duplicate found
        seen.add(n)
    return False  # No duplicates found


# Alternative Solution: Sorting
# Time: O(n log n), Space: O(1) (if sorting in-place)
def contains_duplicate_sorting(nums: List[int]) -> bool:
    """
    Checks for duplicates by sorting the array first.

    If any duplicates exist, they will be adjacent after sorting. This method
    is useful if memory is a major constraint, as it avoids the extra space
    of a hash set. However, it modifies the input list.
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# Alternative Solution: Brute Force
# Time: O(n^2), Space: O(1)
def contains_duplicate_bruteforce(nums: List[int]) -> bool:
    """
    Checks for duplicates using nested loops to compare every pair.

    This is the most straightforward but least efficient approach. It's too
    slow for large inputs but simple to understand and write.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# Alternative Solution: One-liner with Set
# Time: O(n), Space: O(n)
def contains_duplicate_oneliner(nums: List[int]) -> bool:
    """
    Checks for duplicates by comparing the length of the list to a set of it.

    This is the most concise way to write the hash set solution in Python.
    It's functionally identical to the optimal solution but less explicit,
    as it builds the entire set first.
    """
    return len(nums) != len(set(nums))


# --- Tests ---
if __name__ == "__main__":
    # Test cases
    test1 = [1, 2, 3, 1]
    test2 = [1, 2, 3, 4]
    test3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    test4 = []
    test5 = [1]

    # Optimal solution
    assert contains_duplicate(test1) is True
    assert contains_duplicate(test2) is False
    assert contains_duplicate(test3) is True
    assert contains_duplicate(test4) is False
    assert contains_duplicate(test5) is False

    # Sorting solution - use copies to avoid modifying the list for next tests
    assert contains_duplicate_sorting(test1[:]) is True
    assert contains_duplicate_sorting(test2[:]) is False
    assert contains_duplicate_sorting(test3[:]) is True
    assert contains_duplicate_sorting(test4[:]) is False
    assert contains_duplicate_sorting(test5[:]) is False

    # Brute-force solution
    assert contains_duplicate_bruteforce(test1) is True
    assert contains_duplicate_bruteforce(test2) is False
    assert contains_duplicate_bruteforce(test3) is True
    assert contains_duplicate_bruteforce(test4) is False
    assert contains_duplicate_bruteforce(test5) is False

    # One-liner solution
    assert contains_duplicate_oneliner(test1) is True
    assert contains_duplicate_oneliner(test2) is False
    assert contains_duplicate_oneliner(test3) is True
    assert contains_duplicate_oneliner(test4) is False
    assert contains_duplicate_oneliner(test5) is False

    print("All tests passed!")
