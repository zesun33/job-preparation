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


# Example Usage:
# s = "anagram"
# t = "nagaram"
# solver = Solution()
# print(f"Sorting method: {solver.isAnagram_sorting(s, t)}")
# print(f"Hash map method: {solver.isAnagram_hashMap(s, t)}")
# print(f"Manual hash map method: {solver.isAnagram_hashMap_manual(s, t)}")

# s = "rat"
# t = "car"
# print(f"Sorting method: {solver.isAnagram_sorting(s, t)}")
# print(f"Hash map method: {solver.isAnagram_hashMap(s, t)}")
# print(f"Manual hash map method: {solver.isAnagram_hashMap_manual(s, t)}")
