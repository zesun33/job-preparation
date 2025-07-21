# Score of a String - Teaching Notes

**Problem:** [Score of a String - LeetCode](https://leetcode.com/problems/score-of-a-string/description/)

**Topic:** String Processing, ASCII Values, Basic Iteration

---

## 1. Intuitive Overview

Think of this like measuring the "distance" between letters in the alphabet.

Imagine you have a string like "hello". You want to find out how "far apart" each pair of neighboring letters are from each other. Just like measuring the distance between two houses on a street, we measure the distance between letters using their position in the alphabet.

For example:

- 'h' and 'e' are some distance apart
- 'e' and 'l' are some distance apart
- 'l' and 'l' are right next to each other (distance = 0)
- 'l' and 'o' are some distance apart

We add up all these distances to get the total "score" of the string.

---

## 2. Step-by-Step Explanation

Let's build this solution step by step:

**Step 1: Understanding ASCII Values**

- Every character on your keyboard has a number assigned to it called an ASCII value
- 'a' = 97, 'b' = 98, 'c' = 99, and so on
- The `ord()` function in Python gives us this number: `ord('a')` returns 97

**Step 2: Finding Distance Between Characters**

- To find distance between 'h' and 'e': `abs(ord('h') - ord('e'))`
- `ord('h')` = 104, `ord('e')` = 101
- Distance = `abs(104 - 101)` = 3

**Step 3: Process All Adjacent Pairs**

- Go through the string from left to right
- For each character, compare it with the next character
- Add up all the distances

**Step 4: Handle the Loop**

- If string has length n, we need to check n-1 pairs
- Use `range(len(s) - 1)` to avoid going out of bounds

---

## 3. Visual/Mental Model

Picture the string "hello":

```
h  e  l  l  o
|  |  |  |  |
104 101 108 108 111

Distances:
h→e: |104-101| = 3
e→l: |101-108| = 7
l→l: |108-108| = 0
l→o: |108-111| = 3

Total: 3 + 7 + 0 + 3 = 13
```

Think of it like a ruler measuring gaps between letters on a number line.

---

## 4. Code (Optimal Solution)

```python
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
```

**Key Points:**

- `ord(s[i])` gets the ASCII value of character at position i
- `abs()` ensures we get positive distance (absolute value)
- `range(len(s) - 1)` prevents index out of bounds error

---

## 5. Complexity (Optimal Solution)

**Time Complexity:** We visit each character in the string exactly once, so this takes linear time. In Big-O notation: O(n) where n is the length of the string.

**Space Complexity:** We only use a few variables (total_score, diff, i) regardless of input size, so this uses constant extra space. In Big-O notation: O(1).

---

## 6. Alternative Solutions & Trade-offs

### Alternative 1: Using Sum with Generator Expression

**Approach:** Use Python's built-in `sum()` function with a generator expression.

```python
def scoreOfString(s):
    return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))
```

**Complexity:**

- Time: O(n) - same as optimal
- Space: O(1) - same as optimal

**Trade-offs:**

- More concise and "Pythonic"
- Slightly less readable for beginners
- Same performance as the loop version

### Alternative 2: Using Zip Function

**Approach:** Use `zip()` to pair adjacent characters.

```python
def scoreOfString(s):
    return sum(abs(ord(a) - ord(b)) for a, b in zip(s, s[1:]))
```

**Complexity:**

- Time: O(n) - same performance
- Space: O(n) - creates a slice `s[1:]` which uses extra memory

**Trade-offs:**

- Very concise and elegant
- Uses more memory due to string slicing
- Might be confusing for beginners (what is `zip()`?)

---

## 7. Python Implementation Details

**Built-in Functions Used:**

- `ord()`: Converts a character to its ASCII/Unicode value
  - Example: `ord('a')` returns 97
  - This is how Python represents characters internally as numbers
- `abs()`: Returns the absolute value (always positive)
  - Example: `abs(-5)` returns 5, `abs(5)` returns 5
- `len()`: Returns the length of a string
- `range()`: Creates a sequence of numbers for iteration

**Why ASCII Values Work:**

- ASCII (American Standard Code for Information Interchange) assigns each character a unique number
- Letters are arranged consecutively: 'a'=97, 'b'=98, 'c'=99, etc.
- This makes it easy to calculate "distance" between letters mathematically

**No Special Libraries Needed:**

- This problem uses only basic Python built-ins
- No imports required (like `math`, `collections`, etc.)

---

## 8. Edge Cases

**Edge Case 1: Single Character String**

- Input: `"a"`
- Expected: `0`
- Why: No adjacent pairs exist, so score is 0
- How algorithm handles: `range(len(s) - 1)` = `range(0)` = empty loop

**Edge Case 2: Identical Adjacent Characters**

- Input: `"aaa"`
- Expected: `0` (|a-a| + |a-a| = 0 + 0 = 0)
- Why: Distance between identical characters is 0
- How algorithm handles: `abs(ord('a') - ord('a'))` = `abs(97 - 97)` = 0

**Edge Case 3: Maximum Distance Characters**

- Input: `"az"`
- Expected: `25` (|a-z| = |97-122| = 25)
- Why: 'a' and 'z' are furthest apart in lowercase alphabet
- How algorithm handles: `abs(97 - 122)` = 25

**Edge Case 4: Mixed Case (if allowed)**

- Input: `"aZ"`
- Expected: `57` (|a-Z| = |97-90| = 7... wait, that's wrong!)
- Actually: `abs(97 - 90)` = 7
- Note: Uppercase letters have different ASCII values ('A'=65, 'Z'=90)

---

## 9. Tiny Quiz

Test your understanding with these questions (try before looking at solutions):

**Question 1:** What would be the score of the string "abc"?

- Walk through each step: what are the ASCII values and differences?

**Question 2:** Why do we use `range(len(s) - 1)` instead of `range(len(s))`?

- What would happen if we used the wrong range?

**Question 3:** What's the difference between `ord('A')` and `ord('a')`?

- Which one has a larger ASCII value?

**Question 4:** If we have the string "zzaa", what pairs are we comparing and what's the total score?

- List each pair and its contribution to the final score.

---

_Try answering these questions, then let me know when you're ready for the solutions!_
