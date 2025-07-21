"""
Concatenation of Array - NeetCode Test Problem
https://neetcode.io/problems/concatenation-of-array

Given an integer array nums of length n, return an array ans of length 2n 
where ans[i] == nums[i] and ans[i + n] == nums[i].
"""


def getConcatenation(nums):
    """
    Concatenate array with itself using list addition.
    Time: O(n), Space: O(n)
    """
    return nums + nums


def getConcatenationLoop(nums):
    """
    Alternative: Build result using a loop.
    Time: O(n), Space: O(n)
    """
    result = []
    # Add original array
    for num in nums:
        result.append(num)
    # Add copy of array
    for num in nums:
        result.append(num)
    return result


def getConcatenationExtend(nums):
    """
    Alternative: Use extend method.
    Time: O(n), Space: O(n)
    """
    result = nums.copy()  # Create a copy first
    result.extend(nums)  # Add nums to the end
    return result


def main():
    # Test cases
    test_cases = [
        [1, 2, 1],  # Expected: [1, 2, 1, 1, 2, 1]
        [1, 3, 2, 1],  # Expected: [1, 3, 2, 1, 1, 3, 2, 1]
        [5],  # Expected: [5, 5]
        [],  # Expected: []
        [1, 2, 3, 4, 5],  # Expected: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    ]

    for i, nums in enumerate(test_cases):
        print(f"Test {i + 1}: {nums}")
        result1 = getConcatenation(nums)
        result2 = getConcatenationLoop(nums)
        result3 = getConcatenationExtend(nums)

        print(f"  List addition: {result1}")
        print(f"  Loop method:   {result2}")
        print(f"  Extend method: {result3}")
        print(f"  All match: {result1 == result2 == result3}")
        print()


if __name__ == "__main__":
    main()
