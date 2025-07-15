# Subarray Sum Equals K – Study Note

**Problem:** Given an array of integers `nums` and an integer `k`, return *the total number of continuous subarrays whose sum equals to `k`*.

**Links:** [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/) | [NeetCode](https://neetcode.io/problems/subarray-sum-equals-k?list=neetcode150)

---

### 1. Intuitive Overview (The Transaction Analogy)

Imagine you have a list of financial transactions (positive for deposits, negative for withdrawals). You want to find out how many times a *consecutive sequence* of transactions resulted in a specific net change (e.g., a net gain of $50).

You're not looking at the total account balance, but rather finding every possible segment of your transaction history that adds up exactly to the target value `k`. The brute-force way is to check every single possible segment, but there's a much more clever way to do it by keeping a running total and using a map to remember past totals.

---

### 2. Optimal Solution: Prefix Sum with Hash Map

This approach allows us to solve the problem in a single pass through the array.

#### Step-by-Step Explanation
1.  **Initialize a Collector:** Create a hash map (a dictionary in Python) called `prefix_sum_map`. This map will store each running total (`prefix_sum`) we calculate and the *frequency* (how many times) we've seen that total. We start it with `{0: 1}`. This is a crucial trick to handle subarrays that start from the very beginning of the array.
2.  **Keep a Running Total:** Initialize a `current_sum` variable to 0. We'll iterate through the `nums` array, adding each number to this `current_sum`.
3.  **The Key Insight:** As we compute our `current_sum` at each position, the goal is to find if a previous running sum exists such that `current_sum - previous_sum = k`. By rearranging the formula, we get `previous_sum = current_sum - k`.
4.  **Check the Map:** For each `current_sum`, we check if the `prefix_sum_map` contains the key `current_sum - k`.
    - If **yes**, it means a subarray ending at the current position sums to `k`. The number of times we've seen that `previous_sum` is the number of new subarrays we just found. We add this frequency to our total `count`.
    - If **no**, we continue.
5.  **Update the Map:** After checking, we update the map with the `current_sum` we just calculated, incrementing its count.
6.  **Finish the Loop:** After iterating through all the numbers, the `count` will hold the total number of subarrays that sum to `k`.

#### Visual Model
Picture your `current_sum` as your position on a number line. You start at 0.
- `nums = [1, 2, 3, 1]`, `k = 3`
- **Start:** `current_sum = 0`, `count = 0`, `map = {0: 1}`
- **`num = 1`**:
    - `current_sum` becomes 1.
    - Look for `1 - 3 = -2` in map. Not found.
    - Update map: `map = {0: 1, 1: 1}`.
- **`num = 2`**:
    - `current_sum` becomes `1 + 2 = 3`.
    - Look for `3 - 3 = 0` in map. Found! `map[0]` is 1. So, `count` becomes 1. (This found the subarray `[1, 2]`).
    - Update map: `map = {0: 1, 1: 1, 3: 1}`.
- **`num = 3`**:
    - `current_sum` becomes `3 + 3 = 6`.
    - Look for `6 - 3 = 3` in map. Found! `map[3]` is 1. So, `count` becomes `1 + 1 = 2`. (This found the subarray `[1, 2, 3]` sums to 6, but the subarray `[3]` itself is a valid one). Wait, the subarray is just `[3]`. The prefix sum up to `[1,2]` is 3. `current_sum` is 6. `6-3=3`. The subarray is the part *between* the prefix sums.
    - Update map: `map = {0: 1, 1: 1, 3: 1, 6: 1}`.
- **`num = 1`**:
    - `current_sum` becomes `6 + 1 = 7`.
    - Look for `7 - 3 = 4` in map. Not found.
    - Update map: `map = {0: 1, 1: 1, 3: 1, 6: 1, 7: 1}`.

Final `count` is 2. The subarrays are `[1, 2]` and `[3]`.

#### Code (Optimal Solution)
```python
from typing import List

def subarray_sum_optimal(nums: List[int], k: int) -> int:
    # Map to store {prefix_sum: frequency}
    # Initialized with {0: 1} for subarrays starting at index 0
    prefix_sum_map = {0: 1}
    
    count = 0
    current_sum = 0
    
    for num in nums:
        # Update the running total
        current_sum += num
        
        # Check if a subarray sum `k` can be formed
        diff = current_sum - k
        if diff in prefix_sum_map:
            count += prefix_sum_map[diff]
        
        # Update the map with the current prefix sum
        prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1
            
    return count
```

#### Complexity (Optimal Solution)
- **Time Complexity: `O(n)`**
  - We iterate through the list of `n` numbers only once. Dictionary lookups and insertions are `O(1)` on average.
- **Space Complexity: `O(n)`**
  - In the worst case, all prefix sums are unique, and the hash map will store `n` different keys.

---

### 3. Alternative Solutions & Trade-offs

#### Approach #1: Brute Force (with optimization)
- **Explanation:** Use two loops. The outer loop fixes the start of the subarray (`i`), and the inner loop iterates from `i` to the end of the array, maintaining a running sum for the current subarray.
- **Code:**
  ```python
  def subarray_sum_brute_force(nums: List[int], k: int) -> int:
      count = 0
      for i in range(len(nums)):
          current_sum = 0
          for j in range(i, len(nums)):
              current_sum += nums[j]
              if current_sum == k:
                  count += 1
      return count
  ```
- **Complexity:** Time: `O(n²)`, Space: `O(1)`.
- **Trade-offs:** Much simpler to understand and write, but it will be too slow for large inputs. This version is `O(n²)` instead of `O(n³)` because we avoid recalculating the sum from scratch each time.

---

### 4. Edge Cases
- **Empty array `[]`:** The loop never runs, `count` remains 0. Correct.
- **Array with negative numbers `[1, -1, 1]`, k=0:** The algorithm correctly finds `[1, -1]` as a valid subarray.
- **Array with zeros `[0, 0, 0]`, k=0:** The algorithm correctly counts all 6 subarrays that sum to 0: `[0]` (3 times), `[0, 0]` (2 times), and `[0, 0, 0]` (1 time).

---

### 5. Tiny Quiz
1.  In the optimal solution, why is the `prefix_sum_map` initialized with `{0: 1}`?
2.  If `nums = [1, 1, 1]` and `k = 2`, walk through the state of `current_sum`, `count`, and `prefix_sum_map` at each step.
3.  What is the primary trade-off between the brute-force `O(n²)` solution and the optimal `O(n)` solution?
