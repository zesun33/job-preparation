# Top K Frequent Elements

**Problem:** [Top K Frequent Elements on NeetCode](https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150)

---

### 1. Intuitive Overview

Imagine you have a big bag of colored marbles. Your goal is to find the **two** colors that appear most often.

You would probably dump the marbles on a table and start sorting them into piles, one for each color. After sorting, you'd count how many marbles are in each pile. Finally, you'd look at all your piles, find the two biggest ones, and announce their colors.

This problem is the same, but with numbers instead of marbles. We're given a list of numbers and asked to find the `k` most frequent ones. The core idea is:

1.  **Count** how many times each number appears.
2.  **Find** the `k` numbers with the highest counts.

---

### 2. The Core Data Structure: Bucket Sort

Before diving into the steps, let's understand the main idea. The optimal solution uses a data structure concept called **Bucket Sort**.

- **What is it?** Bucket Sort is a sorting algorithm that works by distributing elements into a number of "buckets." Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sorting algorithm.
- **How does it apply here?** We aren't sorting numbers in the traditional sense (e.g., from smallest to largest). Instead, we are sorting them by their **frequency**. The "buckets" will hold numbers that have the same count. For example, one bucket for all numbers that appear once, another for all numbers that appear twice, and so on.
- **Why is it efficient?** It avoids direct comparisons between elements. Instead of asking "is 3's count greater than 5's count?", we just place `3` and `5` into their respective frequency buckets. This allows us to group elements by the property we care about (frequency) in a single pass, which is very fast (O(n)).

---

### 3. Step-by-Step Explanation (Optimal Solution)

The most efficient way to solve this is using our **Bucket Sort** strategy. It's clever because it avoids a full, slow sort of all the elements.

Let's use the example `nums = [1, 1, 1, 2, 2, 3]` and `k = 2`.

**Step 1: Count Frequencies**

- First, we need to know how many times each number appears. A hash map (or a Python dictionary) is perfect for this.
- We go through the list:
  - See `1`. Add it to the map: `{1: 1}`.
  - See another `1`. Update the map: `{1: 2}`.
  - See a third `1`. Update the map: `{1: 3}`.
  - See `2`. Add it to the map: `{1: 3, 2: 1}`.
  - See another `2`. Update the map: `{1: 3, 2: 2}`.
  - See `3`. Add it to the map: `{1: 3, 2: 2, 3: 1}`.
- After this step, our frequency map is `{1: 3, 2: 2, 3: 1}`.

**Step 2: Create "Frequency Buckets"**

- Now, we create a list of lists (our "buckets"). The **index** of this list will represent the **frequency**. The value at that index will be a list of numbers that have that frequency.
- The maximum possible frequency for any number is the length of the input array. So, we create `len(nums) + 1` empty buckets. For our example `[1,1,1,2,2,3]`, we have 6 elements, so we create 7 buckets (indices 0 through 6).
  ```
  buckets = [
      [],    // index 0: numbers that appear 0 times
      [],    // index 1: numbers that appear 1 time
      [],    // index 2: numbers that appear 2 times
      [],    // index 3: numbers that appear 3 times
      [],    // index 4: ...
      [],    // index 5: ...
      []     // index 6: ...
  ]
  ```
- Now, we go through our frequency map `{1: 3, 2: 2, 3: 1}` and place each number in the correct bucket:
  - Number `1` has a frequency of `3`. Put it in `buckets[3]`.
  - Number `2` has a frequency of `2`. Put it in `buckets[2]`.
  - Number `3` has a frequency of `1`. Put it in `buckets[1]`.
- Our buckets now look like this:
  ```
  buckets = [
      [],       // index 0
      [3],      // index 1
      [2],      // index 2
      [1],      // index 3
      [],       // index 4
      [],       // index 5
      []        // index 6
  ]
  ```

**Step 3: Collect the Results**

- We need the `k` most frequent elements. The highest frequencies are at the end of our `buckets` list.
- We'll create an empty list called `res` (short for "result") to store our final answer.
- We iterate backward from the last bucket (highest frequency) to the first:
  - Start at `buckets[6]`. It's empty.
  - `buckets[5]`. Empty.
  - `buckets[4]`. Empty.
  - `buckets[3]`. It contains `[1]`. Add `1` to `res`. `res` is now `[1]`.
  - We need `k=2` elements, and we only have 1, so we continue.
  - `buckets[2]`. It contains `[2]`. Add `2` to `res`. `res` is now `[1, 2]`.
- We have now found `k=2` elements, so we can stop and return `res`, which is `[1, 2]`.

---

### 3. Visual or Mental Model

Think of a chest of drawers. Each drawer is labeled with a number: "Appears 1 Time", "Appears 2 Times", "Appears 3 Times", etc.

1.  **Counting:** You take your list of numbers and count them up, writing down each number and its count on a sticky note (this is your hash map).
    - `1: 3 times`
    - `2: 2 times`
    - `3: 1 time`
2.  **Bucketing:** You take each sticky note and place the number into the corresponding drawer.
    - The number `1` goes into the "Appears 3 Times" drawer.
    - The number `2` goes into the "Appears 2 Times" drawer.
    - The number `3` goes into the "Appears 1 Time" drawer.
3.  **Collecting:** To find the most frequent, you open the highest-numbered drawer first. You take out all the numbers inside. If you haven't found `k` items yet, you go to the next-highest drawer and repeat until you have `k` items.

This is exactly what the bucket sort algorithm does.

---

### 4. Code (Optimal Solution)

```python
import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Finds the k most frequent elements using a bucket sort approach.
        """
        # Step 1: Count frequency of each number.
        # `count.get(n, 0)` gets the current count of n, or 0 if it's not yet in the map.
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Create frequency buckets.
        # The index of the list represents frequency. The list must be `len(nums) + 1` long
        # because a number could appear up to `len(nums)` times.
        # e.g., nums = [1,1,1,1], len is 4, so we need indices 0,1,2,3,4.
        freq_buckets = [[] for i in range(len(nums) + 1)]

        # Place numbers into buckets based on their count (frequency).
        for n, c in count.items():
            freq_buckets[c].append(n)

        # Step 3: Gather the top k results.
        # `res` is a common convention for the "result" list we are building.
        res = []
        # Iterate backwards from the highest possible frequency.
        for i in range(len(freq_buckets) - 1, 0, -1):
            # For each number in the current frequency bucket...
            for n in freq_buckets[i]:
                res.append(n)
                # If we have found k elements, we are done.
                if len(res) == k:
                    return res
        return res
```

---

### 5. Complexity (Optimal Solution)

- **Time Complexity: O(n)**

  - In plain English, this means the time it takes to run the algorithm grows in a straight line with the number of items in the input list (`n`). If you double the input size, the runtime roughly doubles.
  - **Why?**
    1.  Counting frequencies (`for n in nums`): We loop through the `n` numbers once. This is O(n).
    2.  Populating buckets (`for n, c in count.items()`): In the worst case, every number is unique, so this loop runs `n` times. This is also O(n).
    3.  Gathering results (`for i in range(...)`): This loop also runs at most `n` times in total across all buckets. This is O(n).
  - Since we do these steps one after another, the total time is O(n) + O(n) + O(n) = O(n).

- **Space Complexity: O(n)**
  - This means the memory the algorithm uses also grows in a straight line with the input size.
  - **Why?**
    1.  The `count` hash map can store up to `n` unique numbers. This is O(n) space.
    2.  The `freq_buckets` list can also store `n` numbers spread across the different buckets. This is O(n) space.
  - Total space is O(n) + O(n) = O(n).

---

### 6. Alternative Solutions & Trade-offs

#### a. Sort-Based Approach

This is a very common and intuitive way to solve the problem. It's slightly less performant but often easier to write.

- **Approach:**

  1.  Count the frequency of each number using a hash map.
  2.  Sort the unique numbers based on their frequencies in descending order.
  3.  Take the first `k` elements from the sorted list.

- **Code (Verbose):**
  This version is broken into clear steps, similar to the one in the original explanation.

  ```python
  def topKFrequent_sort_verbose(self, nums: list[int], k: int) -> list[int]:
      # 1. Count frequencies using a Counter for convenience.
      count = collections.Counter(nums)

      # 2. Get the unique numbers from the counter.
      unique_nums = list(count.keys())

      # 3. Sort the unique numbers. The `key` is a function that tells `sort`
      #    *what* to sort by. Here, for each number `n`, we look up its
      #    count in the `count` map. `reverse=True` sorts from high to low.
      unique_nums.sort(key=lambda n: count[n], reverse=True)

      # 4. Return the first k elements.
      return unique_nums[:k]
  ```

- **Code (Concise "Pythonic" Version):**
  This version achieves the same result in a more compact way, which you might see in experienced Python developers' code.

  ```python
  def topKFrequent_sort_concise(self, nums: list[int], k: int) -> list[int]:
      count = collections.Counter(nums)
      # `sorted()` is a function that returns a new sorted list.
      # `key=count.get` is a shortcut. It tells `sorted` to use the `get` method
      # of the `count` dictionary as the key. For each item in `count`, its
      # value (the frequency) is used for sorting.
      return sorted(count, key=count.get, reverse=True)[:k]
  ```

- **Complexity:**

  - **Time: O(n log n)**. The dominant step is sorting. If there are `m` unique numbers, sorting takes `O(m log m)`. In the worst case, all `n` numbers are unique (`m=n`), so complexity is `O(n log n)`.
  - **Space: O(n)**. We need space for the frequency map (`count`) and the list of unique numbers.

- **Trade-offs:**
  - **Pro:** This approach is often **simpler to write and understand**. The logic "count then sort" is very direct.
  - **Con:** It is **slower** than the optimal O(n) bucket sort solution. For very large inputs, the `O(n log n)` sorting step will be noticeably less efficient than the `O(n)` bucketing strategy.

---

### 7. Python Implementation Details

- **`collections.Counter`**: This is a specialized dictionary subclass for counting hashable objects. It's a convenient shortcut for the manual frequency counting loop we did in the optimal solution.
- **`dict.get(key, default)`**: This is a safe way to access a dictionary key. If the `key` exists, it returns its value. If not, it returns the `default` value (e.g., `0`) without raising an error. This is very useful for incrementing counters.
- **List of Lists (`[[] for ...]`):** We use a list comprehension to create our `freq_buckets`. This is a concise way to initialize a list containing multiple empty lists.
- **`lambda` functions:** In the sorting solution, `lambda n: count[n]` creates a small, anonymous function. The `sort` method uses this function to decide the sorting order. For each number `n`, it looks up its frequency in the `count` map and uses that value for comparison.

---

### 8. Edge Cases

1.  **`k` is equal to the number of unique elements:**
    - `nums = [1, 2, 3]`, `k = 3`.
    - The algorithm should return all the unique elements: `[1, 2, 3]` (order may vary). The bucket sort correctly handles this by collecting from all non-empty buckets.
2.  **All elements are the same:**
    - `nums = [7, 7, 7, 7]`, `k = 1`.
    - Frequency map: `{7: 4}`. Buckets: `buckets[4] = [7]`.
    - The algorithm will correctly return `[7]`.
3.  **Ties in frequency:**
    - `nums = [1, 1, 2, 2, 3]`, `k = 2`.
    - Frequencies: `{1: 2, 2: 2, 3: 1}`. `buckets[2]` will contain `[1, 2]`.
    - The algorithm will iterate backward, find bucket `[1, 2]`, and add both to the result. It will return `[1, 2]` since `len(res)` will become `k`. The order between `1` and `2` is not guaranteed, which is acceptable for this problem.

---

### 9. Tiny Quiz

1.  In the bucket sort solution, why is the size of the `freq_buckets` list `len(nums) + 1`?
2.  What is the main reason the bucket sort approach is faster (O(n)) than the sorting-based approach (O(n log n))?
3.  If `nums = [1, 2, 3]` and `k = 2`, what would the frequency map and the buckets look like after Step 2?
4.  What would happen if you used a `defaultdict(int)` from the `collections` module instead of a regular dictionary and the `.get()` method for counting frequencies?
