def scoreOfString(s):
    """
    Calculate the score of a string by summing absolute differences
    between ASCII values of adjacent characters.
    """
    total_score = 0

    for i in range(len(s) - 1):
        # Get ASCII difference between adjacent characters
        diff = abs(ord(s[i]) - ord(s[i + 1]))
        total_score += diff

    return total_score


def main():
    # Test cases
    test_cases = [
        ("hello", 13),  # |h-e| + |e-l| + |l-l| + |l-o| = 4+7+0+3 = 13
        ("zaz", 50),  # |z-a| + |a-z| = 25+25 = 50
        ("a", 0),  # Single character = 0
        ("ab", 1),  # |a-b| = 1
        ("ba", 1),  # |b-a| = 1
        ("abc", 2),  # |a-b| + |b-c| = 1+1 = 2
        ("zzaa", 50),  # |z-z| + |z-a| + |a-a| = 0+25+0 = 25
    ]

    print("Testing Score of String solutions:")
    print("=" * 40)

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = scoreOfString(input_str)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"  Input: '{input_str}'")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        if result != expected:
            print(f"  ERROR: Expected {expected}, got {result}")
        print()


if __name__ == "__main__":
    main()
