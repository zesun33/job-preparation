from collections import Counter


class Solution:
    """
    LeetCode 242: Valid Anagram
    https://leetcode.com/problems/valid-anagram/
    """

    def isAnagram_sorting(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams by sorting them.

        - Time: O(n log n), dominated by the sorting algorithm.
        - Space: O(n) in Python because sorted() creates new lists.
        """
        # 1. Anagrams must have the same length.
        if len(s) != len(t):
            return False

        # 2. Sort both strings. If they are anagrams, the sorted versions
        # will be identical.
        return sorted(s) == sorted(t)

    def isAnagram_hashMap(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams using a hash map (frequency counter).

        - Time: O(n), because we iterate through both strings once.
        - Space: O(1), because the hash map will hold at most 26 keys for
                 lowercase English letters.
        """
        # 1. Anagrams must have the same length.
        if len(s) != len(t):
            return False

        # 2. Create frequency counters for both strings and compare them.
        # collections.Counter is a specialized dictionary for this purpose.
        # This is a concise way to do it.
        return Counter(s) == Counter(t)

    def isAnagram_hashMap_manual(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams using a manually implemented hash map.
        This is often what interviewers want to see you write out.
        """
        if len(s) != len(t):
            return False

        counts = {}
        # Count characters in string s
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        # Decrement counts for characters in string t
        for char in t:
            # If a char from t is not in s or its count is already zero,
            # they can't be anagrams.
            if counts.get(char, 0) == 0:
                return False
            counts[char] -= 1

        return True


def main():
    """
    Test function to verify all anagram implementations work correctly.
    Tests various cases including edge cases.
    """
    solver = Solution()

    # Test cases: (s, t, expected_result, description)
    test_cases = [
        # Basic valid anagrams
        ("anagram", "nagaram", True, "Basic anagram - rearranged letters"),
        ("listen", "silent", True, "Classic anagram example"),
        ("danger", "garden", True, "Another valid anagram"),
        # Invalid anagrams
        ("rat", "car", False, "Different letters"),
        ("hello", "bello", False, "One different letter"),
        ("aab", "abb", False, "Same letters, different frequencies"),
        # Edge cases
        ("", "", True, "Both empty strings"),
        ("a", "", False, "Different lengths - one empty"),
        ("abc", "ab", False, "Different lengths"),
        ("a", "a", True, "Single character match"),
        ("a", "b", False, "Single character mismatch"),
        # Case sensitivity (assuming lowercase only)
        ("abc", "bca", True, "Simple rearrangement"),
        ("abcd", "dcba", True, "Reverse order"),
        # Repeated characters
        ("aabbcc", "abcabc", True, "Multiple repeated chars"),
        ("aaab", "abaa", True, "Same chars, different order"),
        ("aaab", "aabb", False, "Different char frequencies"),
    ]

    print("Testing Valid Anagram Solutions")
    print("=" * 50)

    # Test each method
    methods = [
        ("Sorting", solver.isAnagram_sorting),
        ("Hash Map (Counter)", solver.isAnagram_hashMap),
        ("Manual Hash Map", solver.isAnagram_hashMap_manual),
    ]

    all_passed = True

    for method_name, method in methods:
        print(f"\n{method_name} Method:")
        print("-" * 30)
        method_passed = True

        for s, t, expected, description in test_cases:
            result = method(s, t)
            status = "✓ PASS" if result == expected else "✗ FAIL"

            if result != expected:
                method_passed = False
                all_passed = False

            print(f"{status} | '{s}' & '{t}' -> {result} | {description}")

        print(
            f"Method Result: {'All tests passed!' if method_passed else 'Some tests failed!'}"
        )

    print("\n" + "=" * 50)
    print(
        f"Overall Result: {'All methods passed all tests!' if all_passed else 'Some tests failed!'}"
    )

    # Performance comparison for larger strings
    print("\n" + "=" * 50)
    print("Performance Test (Large Strings):")
    print("-" * 30)

    import time

    # Create large test strings
    large_s = "abcdefghijklmnopqrstuvwxyz" * 1000  # 26,000 chars
    large_t = "zyxwvutsrqponmlkjihgfedcba" * 1000  # Same chars, reversed

    for method_name, method in methods:
        start_time = time.time()
        result = method(large_s, large_t)
        end_time = time.time()

        print(f"{method_name}: {result} (Time: {end_time - start_time:.4f}s)")


if __name__ == "__main__":
    main()
