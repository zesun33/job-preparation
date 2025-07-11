# Contains Duplicate – Study Note

**Problem:** Given an integer array `nums`, return **True** if any value appears *at least twice*, otherwise **False**.

**Links:** [LeetCode](https://leetcode.com/problems/contains-duplicate/) | [NeetCode](https://neetcode.io/problems/duplicate-integer?list=neetcode150)

---

### 1. Intuitive Overview (The Party Analogy)

Imagine you're a bouncer at an exclusive party. Your job is to make sure nobody who was already kicked out gets back in. You have a clipboard (`seen = set()`).

When a guest arrives (`n` in `nums`), you check your clipboard.
- If their name is already on it (`n in seen`), you've caught a duplicate! You can stop and report the issue (`return True`).
- If their name isn't on the list, you add it to your clipboard (`seen.add(n)`) and let them pass.

If you get through the entire line of guests without finding any names already on your list, it means everyone was unique (`return False`). The hash set is your clipboard—it gives you a super-fast way to check if you've seen someone before.

---

### 2. Optimal Solution: Hash Set

This is the most efficient and common solution.

#### Step-by-Step Explanation
1.  **Initialize a Collector:** Create an empty hash set, which we'll call `seen`. This data structure is perfect because adding and checking for an item takes, on average, a constant amount of time, no matter how large it gets.
2.  **Iterate Through Numbers:** Go through each number in the input list `nums`, one by one.
3.  **Check for Duplicates:** For each number, check if it's already in our `seen` set.
    - If **yes**, you've found a number you've encountered before. This is a duplicate. You can immediately stop and return `True`.
    - If **no**, it's the first time you're seeing this number. Add it to the `seen` set to "remember" it.
4.  **Finish the Loop:** If the loop completes without ever finding a duplicate, it means every element was unique. Return `False`.

#### Visual Model
Let's trace `nums = [1, 2, 3, 1]`:

- **Start:** `seen = {}` (empty set)
- **`n = 1`**: Is `1` in `seen`? No. Add it. `seen` is now `{1}`.
- **`n = 2`**: Is `2` in `seen`? No. Add it. `seen` is now `{1, 2}`.
- **`n = 3`**: Is `3` in `seen`? No. Add it. `seen` is now `{1, 2, 3}`.
- **`n = 1`**: Is `1` in `seen`? **Yes!** Stop and `return True`.

#### Code (Optimal Solution)
```python
from typing import List

def contains_duplicate_optimal(nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

#### Complexity (Optimal Solution)
- **Time Complexity: `O(n)`**
  - We iterate through the list of `n` numbers once. Each lookup (`n in seen`) and insertion (`seen.add(n)`) in a hash set takes `O(1)` time on average.
- **Space Complexity: `O(n)`**
  - In the worst-case scenario (all numbers are unique), the `seen` set will grow to store all `n` numbers from the input list.

---

### 3. Alternative Solutions & Trade-offs

#### Approach #1: Brute Force
- **Explanation:** The simplest way. Compare every element with every other element that comes after it.
- **Code:**
  ```python
  def contains_duplicate_bruteforce(nums: List[int]) -> bool:
      n = len(nums)
      for i in range(n):
          for j in range(i + 1, n):
              if nums[i] == nums[j]:
                  return True
      return False
  ```
- **Complexity:** Time: `O(n²)`, Space: `O(1)`.
- **Trade-offs:** Very easy to write and uses no extra memory, but it's too slow for large inputs and will time out on most platforms.

#### Approach #2: Sorting
- **Explanation:** If you sort the list, any duplicates will become neighbors. You can then find them by making a single pass and checking if an element is the same as the one right next to it.
- **Code:**
  ```python
  def contains_duplicate_sorting(nums: List[int]) -> bool:
      nums.sort()  # Sorts the list in-place
      for i in range(len(nums) - 1):
          if nums[i] == nums[i+1]:
              return True
      return False
  ```
- **Complexity:** Time: `O(n log n)` (dominated by the sort), Space: `O(1)` if sorting in-place (though Python's Timsort can use `O(n)` space in some cases).
- **Trade-offs:** A huge improvement over brute-force. It's a good solution if you cannot use extra memory. However, it's slower than the hash set approach and it modifies the original list.

---

### 4. Edge Cases
- **Empty list `[]`:** Returns `False`. The loops in all solutions won't run.
- **Single element `[42]`:** Returns `False`. No other elements to compare against.
- **All elements are the same `[7, 7, 7]`:** Returns `True` very quickly. The hash-set and sorting solutions find the duplicate on the second element.
- **Duplicates are far apart `[1, 5, 2, 8, 3, 9, 2]`**: The hash-set still shines here, but the sorting approach brings them together.

---

### 5. Tiny Quiz
Time to check your understanding!
1. For the input `[10, 20, 30]`, what would be inside the `seen` set just before the hash-set solution returns?
2. If you are not allowed to use extra memory, which of the three solutions is the best choice?
3. Why is the brute-force approach considered `O(n²)`?
4. What is the biggest downside of the sorting approach?