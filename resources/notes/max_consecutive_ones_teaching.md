# Max Consecutive Ones - Complete Teaching Guide

**Problem:** Find the maximum number of consecutive 1s in a binary array.
**Link:** https://neetcode.io/problems/max-consecutive-ones?list=allNC

---

## 1. Intuitive Overview (Plain English Analogy)

Imagine you're looking at a string of Christmas lights where some bulbs are ON (1) and some are OFF (0). You want to find the longest stretch of consecutive lights that are ON.

Think of it like counting steps while walking:

- When you see a lit bulb (1), you take a step forward and count it
- When you see a dark bulb (0), you stop counting and reset your step counter to zero
- You always remember the highest number of steps you've taken in a row

So if your lights look like: ON-ON-OFF-ON-ON-ON, you'd count:

- First stretch: 2 steps (ON-ON)
- Reset at OFF
- Second stretch: 3 steps (ON-ON-ON)
- Answer: 3 (the longest stretch)

---

## 2. Step-by-Step Explanation

Let's build the solution from the simplest idea:

**Step 1: Basic Counting**

- We need to count consecutive 1s as we go through the array
- Keep a running count of current consecutive 1s

**Step 2: Tracking the Maximum**

- We also need to remember the highest count we've seen so far
- Every time we find a 1, we check if our current streak is the new record

**Step 3: Resetting on 0s**

- When we hit a 0, our current streak ends
- Reset the current count to 0, but keep the maximum we've seen

**Step 4: The Algorithm**

- Start with both counters at 0
- For each number in the array:
  - If it's 1: increment current count, update maximum if needed
  - If it's 0: reset current count to 0
- Return the maximum count

---

## 3. Visual/Mental Model

Picture two counters in your head:

```
Array: [1, 1, 0, 1, 1, 1]
       ↑
current_count = 0
max_count = 0

Step by step:
[1, 1, 0, 1, 1, 1]  →  current=1, max=1
 ↑

[1, 1, 0, 1, 1, 1]  →  current=2, max=2
    ↑

[1, 1, 0, 1, 1, 1]  →  current=0, max=2 (reset!)
       ↑

[1, 1, 0, 1, 1, 1]  →  current=1, max=2
          ↑

[1, 1, 0, 1, 1, 1]  →  current=2, max=2
             ↑

[1, 1, 0, 1, 1, 1]  →  current=3, max=3 (new record!)
                ↑

Final answer: 3
```

Think of `current_count` as your "current streak" and `max_count` as your "personal best."

---

## 4. Code (Optimal Solution)

```python
def findMaxConsecutiveOnes(nums):
    max_count = 0      # Our "personal best" record
    current_count = 0  # Our "current streak"

    for num in nums:
        if num == 1:
            current_count += 1  # Extend the streak
            # Check if we beat our record
            max_count = max(max_count, current_count)
        else:  # num == 0
            current_count = 0   # Streak broken, reset

    return max_count
```

**Key Python concepts used:**

- `max()` function: Returns the larger of two numbers
- Simple for loop: Goes through each element once
- Integer variables: Store our counters

---

## 5. Complexity (Optimal Solution)

**Time Complexity:** We visit each element in the array exactly once, doing constant work for each element. If the array has n elements, we do n operations total. This is **O(n)** time.

**Space Complexity:** We only use two integer variables (`max_count` and `current_count`) regardless of how big the input array is. This is **O(1)** space - constant space.

This is optimal because we must look at every element at least once to solve the problem.

---

## 6. Alternative Solutions & Trade-offs

### Alternative 1: Brute Force (Check Every Possible Substring)

**Approach:** For every starting position, count consecutive 1s from that position.

```python
def findMaxConsecutiveOnes_brute_force(nums):
    max_count = 0

    # Try starting from each position
    for i in range(len(nums)):
        current_count = 0
        # Count consecutive 1s starting from position i
        for j in range(i, len(nums)):
            if nums[j] == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                break  # Stop when we hit a 0

    return max_count
```

**Complexity:**

- Time: O(n²) - for each of n positions, we might check up to n elements
- Space: O(1) - still just using a few variables

**Trade-offs:** Much simpler logic but significantly slower. For small arrays it's fine, but for large arrays it becomes impractical.

### Alternative 2: Split and Count

**Approach:** Split the array by 0s, then find the longest segment.

```python
def findMaxConsecutiveOnes_split(nums):
    # Convert to string and split by '0'
    nums_str = ''.join(map(str, nums))
    segments = nums_str.split('0')

    # Find longest segment of 1s
    max_length = 0
    for segment in segments:
        max_length = max(max_length, len(segment))

    return max_length
```

**Complexity:**

- Time: O(n) - converting to string and splitting both take linear time
- Space: O(n) - we create a string and list of segments

**Trade-offs:** More memory usage and string operations make it slower in practice, though theoretically the same time complexity.

---

## 7. Python Implementation Details

**Built-in Functions Used:**

- `max(a, b)`: Returns the larger of two values. This is a built-in function that works with any comparable types (numbers, strings, etc.)
- `range()`: Creates a sequence of numbers for iteration
- `len()`: Returns the length of a sequence

**Core Python Features:**

- **For loops:** `for item in list` iterates through each element
- **Integer arithmetic:** Simple addition and comparison
- **Conditional statements:** `if/else` for branching logic

**Alternative Python Tools:**

- `itertools.groupby()`: Could group consecutive identical elements
- List comprehensions: Could create sublists of consecutive 1s
- Regular expressions: Could find patterns of consecutive 1s

But the simple loop approach is most readable and efficient for this problem.

---

## 8. Edge Cases

**Edge Case 1: All zeros `[0, 0, 0]`**

- No consecutive 1s exist
- Algorithm correctly returns 0 because max_count never gets updated

**Edge Case 2: All ones `[1, 1, 1, 1]`**

- The entire array is one long streak
- current_count keeps growing, max_count keeps updating
- Returns the length of the entire array

**Edge Case 3: Single element arrays `[0]` or `[1]`**

- `[0]`: Returns 0 (no consecutive 1s)
- `[1]`: Returns 1 (one consecutive 1)
- Algorithm handles both correctly with the same logic

**Edge Case 4: Alternating pattern `[1, 0, 1, 0, 1]`**

- Maximum consecutive 1s is just 1
- current_count resets to 0 after each 1, so max_count stays at 1

---

## 9. Tiny Quiz

Test your understanding with these questions:

**Question 1:** What would the algorithm return for the array `[0, 1, 1, 0, 1, 1, 1, 0]`? Walk through the steps.

**Question 2:** Why do we need both `current_count` and `max_count` variables? What would happen if we only used one?

**Question 3:** In the line `max_count = max(max_count, current_count)`, when does `current_count` actually become larger than `max_count`?

**Question 4:** What's the key difference between our optimal O(n) solution and the brute force O(n²) solution in terms of how many times we examine each array element?

Try answering these, then let me know your thoughts! I'll provide feedback and explanations for each.
