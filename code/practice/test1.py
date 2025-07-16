from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        LeetCode 49: Group Anagrams
        https://leetcode.com/problems/group-anagrams/

        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

        Example 1:
            Input: strs = ["eat","tea","tan","ate","nat","bat"]
            Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

        Example 2:
            Input: strs = [""]
            Output: [[""]]

        Example 3:
            Input: strs = ["a"]
            Output: [["a"]]
        """
        anagram_map = {}
        for string in strs:
            sorted_string = sorted(string)
            if sorted_string not in anagram_map:
                anagram_map[sorted_string] = []
            anagram_map[sorted_string].append(string)
        return list(anagram_map.values())

    def groupAnagrams_hashMap(self, strs: List[str]) -> List[List[str]]:
        """
        LeetCode 49: Group Anagrams
        https://leetcode.com/problems/group-anagrams/

        HashMap approach:
        Use a hash map (dictionary) to group words by their character counts.
        The key is a tuple representing the frequency of each letter (a-z).
        Words with the same letter counts are anagrams and will share the same key.
        """
        from collections import defaultdict

        anagram_map = defaultdict(list)
        for word in strs:
            # Create a count of each character (assuming lowercase a-z)
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagram_map[key].append(word)
        return list(anagram_map.values())

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))
    print(sol.groupAnagrams_hashMap(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams_hashMap([""]))
    print(sol.groupAnagrams_hashMap(["a"]))
