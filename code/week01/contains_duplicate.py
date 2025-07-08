"""Contains Duplicate - NeetCode 150 #1

Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.

LeetCode Link: https://leetcode.com/problems/contains-duplicate/
"""
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    Return True if any integer appears at least twice in the list, else False.

    Explanation:
    - We use a set called 'seen' to keep track of the numbers we've encountered so far.
    - As we iterate through each number in 'nums':
        - If the number is already in 'seen', it means we've found a duplicate, so we return True immediately.
        - If not, we add the number to 'seen' and continue.
    - If we finish checking all numbers without finding any duplicates, we return False.

    Why use a set?
    - Sets in Python provide O(1) average time complexity for lookups and insertions.
    - This makes the solution efficient: O(n) time and O(n) space, where n is the length of 'nums'.
    """
    seen = set()
    for n in nums:
        if n in seen:
            return True  # Duplicate found
        seen.add(n)
    return False  # No duplicates found


# basic sanity tests
if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) is True
    print("All tests passed!")