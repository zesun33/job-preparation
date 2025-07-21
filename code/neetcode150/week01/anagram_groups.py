# Anagram Groups (Group Anagrams)
# Problem: https://neetcode.io/problems/anagram-groups


def groupAnagrams(strs):
    """
    Group anagrams together using sorted string as key.

    Args:
        strs: List of strings to group
    Returns:
        List of lists, where each inner list contains anagrams
    """
    # Dictionary to store groups: sorted_string -> list_of_anagrams
    anagram_groups = {}

    for word in strs:
        # Create signature by sorting letters
        # "eat" becomes "aet", "tea" becomes "aet"
        signature = "".join(sorted(word))

        # If we've seen this signature before, add to existing group
        # Otherwise, create new group
        if signature in anagram_groups:
            anagram_groups[signature].append(word)
        else:
            anagram_groups[signature] = [word]

    # Return all groups as a list of lists
    return list(anagram_groups.values())


def groupAnagrams_counting(strs):
    """Alternative: Use character counting instead of sorting"""
    from collections import defaultdict

    anagram_groups = defaultdict(list)

    """
    Group anagrams together using character counting as a signature.
    
    Instead of sorting, this approach counts the frequency of each character
    in each word and uses that count as a signature. Words with the same
    character frequencies are anagrams of each other.
    
    Args:
        strs: List of strings to group
    Returns:
        List of lists, where each inner list contains anagrams
    """
    for word in strs:
        # Count frequency of each character
        char_count = [0] * 26  # for a-z
        for char in word:
            char_count[ord(char) - ord("a")] += 1

        # Use tuple of counts as signature
        signature = tuple(char_count)
        anagram_groups[signature].append(word)

    return list(anagram_groups.values())


def groupAnagrams_bruteforce(strs):
    """Brute force: compare all pairs"""

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)

    result = []
    used = [False] * len(strs)

    for i in range(len(strs)):
        if used[i]:
            continue

        group = [strs[i]]
        used[i] = True

        for j in range(i + 1, len(strs)):
            if not used[j] and are_anagrams(strs[i], strs[j]):
                group.append(strs[j])
                used[j] = True

        result.append(group)

    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: Basic example
    test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = groupAnagrams(test1)
    print("Test 1:", result1)
    # Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    # Test case 2: Empty string
    test2 = [""]
    result2 = groupAnagrams(test2)
    print("Test 2:", result2)
    # Expected: [['']]

    # Test case 3: All different
    test3 = ["abc", "def", "ghi"]
    result3 = groupAnagrams(test3)
    print("Test 3:", result3)
    # Expected: [['abc'], ['def'], ['ghi']]

    # Test case 4: All same anagrams
    test4 = ["abc", "bca", "cab"]
    result4 = groupAnagrams(test4)
    print("Test 4:", result4)
    # Expected: [['abc', 'bca', 'cab']]

    # Test case 5: Single characters
    test5 = ["a", "b", "a"]
    result5 = groupAnagrams(test5)
    print("Test 5:", result5)
    # Expected: [['a', 'a'], ['b']]
