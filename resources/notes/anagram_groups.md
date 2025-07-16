# Anagram Groups - Learning Guide

**Topic / Problem:**
Group Anagrams - Given an array of strings, group anagrams together.
Link: https://neetcode.io/problems/anagram-groups

**My current level:**
• I understand the basic idea of variables, loops, and functions in Python.
• I'm NOT yet comfortable with formal proofs, asymptotic math, or complex jargon.

---

## 1. Intuitive Overview (Plain-English Analogy)

Imagine you have a pile of word cards scattered on a table. Your job is to organize them into groups where each group contains words that use the exact same letters (just rearranged).

Think of it like sorting Scrabble tiles:
- "eat", "tea", "ate" all use letters E, A, T → same group
- "bat", "tab" both use letters B, A, T → same group  
- "cat" uses C, A, T → different group (has C instead of E)

It's like being a librarian who needs to organize books by their content, not their title order.

---

## 2. Step-by-Step Explanation

**Step 1:** Look at each word and figure out its "signature"
**Step 2:** Words with the same signature belong together
**Step 3:** Use a dictionary to collect words by their signature

**What's a signature?** It's a way to identify anagrams:
- Sort the letters: "eat" → "aet", "tea" → "aet", "ate" → "aet"
- All anagrams have the same sorted letters!

**Why does this work?**
- Anagrams use identical letters, just rearranged
- When we sort letters alphabetically, anagrams become identical
- We can use this sorted version as a "key" to group them

---

## 3. Visual/Mental Model

Picture a filing cabinet with drawers:

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

Processing:
"eat" → sort → "aet" → goes to drawer "aet"
"tea" → sort → "aet" → goes to drawer "aet" 
"tan" → sort → "ant" → goes to drawer "ant"
"ate" → sort → "aet" → goes to drawer "aet"
"nat" → sort → "ant" → goes to drawer "ant"
"bat" → sort → "abt" → goes to drawer "abt"

Final filing cabinet:
Drawer "aet": [eat, tea, ate]  ← all sort to "aet"
Drawer "ant": [tan, nat]       ← all sort to "ant"  
Drawer "abt": [bat]            ← sorts to "abt"

Result: [[eat, tea, ate], [tan, nat], [bat]]
```

---

## 4. Code (Optimal Solution)

```python
def groupAnagrams(strs):
    # Dictionary to store groups: sorted_string -> list_of_anagrams
    anagram_groups = {}
    
    for word in strs:
        # Create signature by sorting letters
        signature = ''.join(sorted(word))
        
        # Add to existing group or create new group
        if signature in anagram_groups:
            anagram_groups[signature].append(word)
        else:
            anagram_groups[signature] = [word]
    
    # Return all groups as a list of lists
    return list(anagram_groups.values())
```

---

## 5. Complexity (Optimal Solution)

**Time Complexity:** We visit each word once, and for each word we sort its letters.
- If we have N words and the longest word has M letters
- Sorting each word takes M log M time  
- We do this for all N words
- Total: N × M log M
- **Big-O: O(N × M log M)**

**Space Complexity:** We store all words in our dictionary, plus the sorted signatures.
- We store N words total
- Each signature is at most M characters
- **Big-O: O(N × M)**

---

## 6. Alternative Solutions & Trade-offs

### a) Character Count Approach
**Idea:** Instead of sorting, count each letter's frequency.
- "eat" → {e:1, a:1, t:1}, "tea" → {e:1, a:1, t:1}

```python
def groupAnagrams_counting(strs):
    from collections import defaultdict
    anagram_groups = defaultdict(list)
    
    for word in strs:
        # Count frequency of each character
        char_count = [0] * 26  # for a-z
        for char in word:
            char_count[ord(char) - ord('a')] += 1
        
        # Use tuple of counts as signature
        signature = tuple(char_count)
        anagram_groups[signature].append(word)
    
    return list(anagram_groups.values())
```

**Complexity:**
- Time: O(N × M) - no sorting needed
- Space: O(N × M) - same storage

**Trade-off:** Faster but more complex code, only works for lowercase a-z

### b) Brute Force Approach
**Idea:** Compare every word with every other word to check if they're anagrams.

```python
def groupAnagrams_bruteforce(strs):
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
```

**Complexity:**
- Time: O(N² × M log M) - compare all pairs, sort for each comparison
- Space: O(N × M) - store result

**Trade-off:** Much slower, but easier to understand logic

---

## 7. Python Implementation Details

**Key Python features used:**
- `dict`: Store groups with signature as key
- `sorted()`: Built-in function that returns sorted list of characters
- `''.join()`: Converts list of characters back to string
- `list.values()`: Gets all values from dictionary
- `collections.defaultdict`: Automatically creates empty lists for new keys
- `ord()`: Gets ASCII value of character (for counting approach)
- `tuple()`: Immutable sequence that can be used as dictionary key

**Alternative implementations in Python:**
- `collections.Counter`: Could count character frequencies
- `collections.defaultdict(list)`: Cleaner than checking if key exists

---

## 8. Edge Cases

1. **Empty input:** `[]` → return `[]`
2. **Single word:** `["abc"]` → `[["abc"]]`
3. **All same anagrams:** `["abc", "bca", "cab"]` → `[["abc", "bca", "cab"]]`
4. **Empty strings:** `["", ""]` → `[["", ""]]`
5. **Single characters:** `["a", "b", "a"]` → `[["a", "a"], ["b"]]`
6. **Mixed lengths:** `["a", "aa", "aaa"]` → `[["a"], ["aa"], ["aaa"]]`

**How the algorithm handles them:**
- Empty strings sort to empty strings (same signature)
- Single characters are their own signature
- Different lengths can't be anagrams (different signatures)

---

## 9. Tiny Quiz

Test your understanding with these questions:

**a)** What would be the signature for the word "listen"?

**b)** If you have `["abc", "def", "fed"]`, how many groups would you get?

**c)** Why do we use sorted letters as the signature instead of just the original word?

**d)** What happens if two different words have the same sorted signature?

---

*Don't peek at the answers until you try! Think through each question step by step.*