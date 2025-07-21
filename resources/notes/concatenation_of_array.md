# Concatenation of Array - Teaching Notes

**Problem:** [Concatenation of Array](https://neetcode.io/problems/concatenation-of-array)

Given an integer array `nums` of length n, return an array `ans` of length 2n where `ans[i] == nums[i]` and `ans[i + n] == nums[i]`.

---

## 1. Intuitive Overview

Think of this like making a photocopy of a list and taping it to the end of the original.

**Real-world analogy:** Imagine you have a playlist of 3 songs: [Song A, Song B, Song C]. You want to create a "double playlist" that plays the same songs twice in a row: [Song A, Song B, Song C, Song A, Song B, Song C].

That's exactly what this problem asks - take an array and stick a copy of itself at the end.

---

## 2. Step-by-Step Explanation

Let's build up to the solution:

**Step 1:** Understand what "concatenation" means

- Concatenation = joining two things together end-to-end
- Like gluing two pieces of string together

**Step 2:** Identify the pattern

- Original array: [1, 2, 3]
- We want: [1, 2, 3, 1, 2, 3]
- Notice: first half = original, second half = copy of original

**Step 3:** Think about the solution

- We need to create a new array that's twice as long
- Fill first half with original elements
- Fill second half with the same elements again

---

## 3. Visual/Mental Model

Picture it like this:

```
Original array:  [1, 2, 3]
                  ↓  ↓  ↓
Result array:    [1, 2, 3, 1, 2, 3]
                  ↑  ↑  ↑  ↑  ↑  ↑
                  |  |  |  |  |  |
                  original  copy
```

Or think of it as two boxes side by side:

```
Box 1 (original): [1, 2, 3]
Box 2 (copy):     [1, 2, 3]
Combined:         [1, 2, 3, 1, 2, 3]
```

---

## 4. Code (Optimal Solution)

```python
def getConcatenation(nums):
    """
    Concatenate array with itself using list addition.
    Time: O(n), Space: O(n)
    """
    return nums + nums
```

**How it works:**

- In Python, `+` operator on lists means "join them together"
- `[1, 2] + [3, 4]` gives `[1, 2, 3, 4]`
- `nums + nums` joins the array with itself
- Super simple and readable!

---

## 5. Complexity (Optimal Solution)

**Time Complexity:** We visit each element once to copy it

- In plain English: "We need to look at every number in the original array exactly once to copy it"
- Big-O notation: O(n) where n is the length of the input array

**Space Complexity:** We create a new array twice the size of the original

- In plain English: "We need twice as much memory as the original array takes up"
- Big-O notation: O(n) for the result array (we don't count input space)

---

## 6. Alternative Solutions & Trade-offs

### Approach A: Loop Method (Manual Building)

**Explanation:** Build the result step by step using loops.

```python
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
```

**Complexity:**

- Time: O(n) - we loop through the array twice, but that's still linear
- Space: O(n) - same space as optimal solution

**Trade-offs:**

- More verbose but shows the logic clearly
- Good for understanding what's happening step-by-step
- Slightly slower due to individual append operations

### Approach B: Extend Method

**Explanation:** Use Python's `extend()` method to add elements.

```python
def getConcatenationExtend(nums):
    """
    Alternative: Use extend method.
    Time: O(n), Space: O(n)
    """
    result = nums.copy()  # Create a copy first
    result.extend(nums)   # Add nums to the end
    return result
```

**Complexity:**

- Time: O(n) - copy operation + extend operation
- Space: O(n) - same as others

**Trade-offs:**

- More explicit about creating a copy first
- `extend()` is efficient for adding multiple elements
- Good middle ground between simplicity and clarity

---

## 7. Python Implementation Details

**Built-in features used:**

**List Addition (`+` operator):**

- Python's `+` operator for lists creates a new list
- `[1, 2] + [3, 4]` returns `[1, 2, 3, 4]`
- Does NOT modify the original lists
- This is called "concatenation" in Python

**List Methods:**

- `append(item)`: adds one item to the end of a list
- `extend(iterable)`: adds all items from another list/iterable to the end
- `copy()`: creates a shallow copy of the list

**Alternative implementations in Python's standard library:**

- `itertools.chain(nums, nums)` - but you'd need to convert to list
- List comprehension: `[x for _ in range(2) for x in nums]`
- Using `*` operator: `[*nums, *nums]` (Python 3.5+)

---

## 8. Edge Cases

**Edge Case 1: Empty Array**

- Input: `[]`
- Expected: `[]`
- How it's handled: `[] + []` = `[]` ✓

**Edge Case 2: Single Element**

- Input: `[5]`
- Expected: `[5, 5]`
- How it's handled: `[5] + [5]` = `[5, 5]` ✓

**Edge Case 3: Large Numbers**

- Input: `[1000000, -1000000]`
- Expected: `[1000000, -1000000, 1000000, -1000000]`
- How it's handled: List addition works with any integers ✓

**Edge Case 4: Very Long Array**

- Input: Array with 1000 elements
- Expected: Array with 2000 elements
- How it's handled: Python handles this efficiently, no special logic needed ✓

---

## 9. Tiny Quiz

Test your understanding! Try to answer these before looking at solutions:

**Question 1:** If `nums = [7, 8, 9]`, what will `nums + nums` return?

**Question 2:** What's the difference between `append()` and `extend()` when building the result?

**Question 3:** If the input array has 100 elements, how many elements will the result have?

**Question 4:** Why do we say the space complexity is O(n) and not O(2n)?

---

_Try answering these questions, then let me know your answers and I'll provide feedback!_
