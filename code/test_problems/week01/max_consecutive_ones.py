def findMaxConsecutiveOnes(nums):
    """
    Find the maximum number of consecutive 1s in a binary array.

    Args:
        nums: List of integers (0s and 1s only)

    Returns:
        int: Maximum number of consecutive 1s
    """
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


def main():
    # Test cases
    test_cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0, 0, 0], 0),
        ([1, 1, 1, 1], 4),
        ([0], 0),
        ([1], 1),
        ([1, 0], 1),
        ([0, 1], 1),
        ([1, 1, 0, 0, 1, 1, 1, 1, 0, 1], 4),
    ]

    print("Testing Max Consecutive Ones:")
    for i, (nums, expected) in enumerate(test_cases):
        result = findMaxConsecutiveOnes(nums)
        status = "✓" if result == expected else "✗"
        print(
            f"Test {i+1}: {status} Input: {nums} → Output: {result} (Expected: {expected})"
        )


if __name__ == "__main__":
    main()
