# Two Sum (LeetCode #1)

## 1. Intuitive Overview (No Code)
Imagine you're at a bookstore with a gift card for a specific amount, say, $20. You want to buy exactly two books that add up to this amount.

The "brute-force" way to do this is to pick the first book, then go through every single other book on the shelf to see if its price adds up to $20. If not, you put the first book back, pick the second book, and check all the *other* books again. This is slow and repetitive.

A much smarter way is to use a "memory list." You pick up the first book, which costs $8. You think, "To reach $20, I need a book that costs exactly $12." You jot down "$8 is at position 1" on your memory list. Then, you pick up the second book. It costs $12. You ask yourself, "What price do I need to make a pair with this one?" The answer is $8. You quickly glance at your memory list and see "Aha! I've already seen an $8 book!" You've found your pair without re-checking every book on the shelf.

This "memory list" is what we'll use in our optimal solution.

## 2. Step-by-Step Explanation (Optimal Solution)
The most efficient algorithm uses a hash map (which is just a Python dictionary) to act as our "memory list."

1.  **Create an empty dictionary.** We'll use it to store each number we see from the input list and its position (its "index"). Let's call it `seen_numbers`.
2.  **Loop through the input list** one number at a time. For each number, we'll call it `current_number`.
3.  **Calculate the difference.** For each `current_number`, we calculate the other number we'd need to find: `difference = target - current_number`.
4.  **Check your memory.** We immediately look in our `seen_numbers` dictionary to see if the `difference` is already there.
5.  **If it's there, you're done!** We've found the pair. The answer is the index of the `difference` (which we stored in our dictionary) and the index of the `current_number`.
6.  **If it's not there, store the current number.** We add the `current_number` and its index to the `seen_numbers` dictionary. This way, it becomes part of our memory for the next numbers in the list to check against.
7.  **Repeat.** Continue until a pair is found.

## 3. Visual or Mental Model
Picture a table with two columns: "Number Seen" and "Position". This table is our dictionary.

Let's say `nums = [2, 7, 11, 15]` and `target = 9`.

1.  **Start:** The table is empty.
2.  **First number is 2:** We need `9 - 2 = 7`. Is `7` in our table? No. So, we add `2` and its position `0` to the table.
    *   Table: `{"Number Seen": 2, "Position": 0}`
3.  **Second number is 7:** We need `9 - 7 = 2`. Is `2` in our table? Yes! It's at position `0`. We found our pair: the current number `7` (at position `1`) and the number `2` (at position `0`).
4.  **Result:** `[0, 1]`.

## 4. Code (Optimal Solution)
Here is a clean Python implementation of the optimal approach.

```python
def two_sum_optimal(nums: list[int], target: int) -> list[int] | None:
    """
    Finds two numbers in a list that add up to a target value using a hash map.
    This is the optimal solution with O(n) time complexity.
    """
    seen_numbers = {}  # Dictionary to store number -> index
    # 'enumerate' gives us both the index (i) and the value (num)
    for i, num in enumerate(nums):
        # Calculate the number we need to find to make the target
        difference = target - num
        # Check if we've seen this required number before
        if difference in seen_numbers:
            # If yes, we found our pair
            return [seen_numbers[difference], i]
        # If not, add the current number and its index to our memory
        seen_numbers[num] = i
    return None # Should not be reached based on problem description
```

## 5. Complexity (Optimal Solution)
*   **Time Complexity: O(n) - Linear Time**
    *   In simple terms, we only have to go through the list of numbers **once**. If the list has 10 numbers (n=10), we do about 10 steps. If it has 1 million numbers (n=1,000,000), we do about 1 million steps. The time it takes grows in a straight line with the size of the input. Looking up a number in a dictionary is, on average, extremely fast and doesn't depend on the list size.
*   **Space Complexity: O(n) - Linear Space**
    *   This refers to how much memory the algorithm uses. In the worst-case scenario, we might have to store every single number from the input list in our `seen_numbers` dictionary before finding a pair. So, the memory needed grows in a straight line with the size of the input list.

## 6. Alternative Solutions & Trade-offs

### Brute-Force Method
*   **a. Approach:** This is the most straightforward, "common sense" method. You use two loops. The outer loop picks a number. The inner loop then checks every *other* number after it to see if they add up to the target.
*   **b. Code and Complexity:**
    ```python
    def two_sum_brute_force(nums: list[int], target: int) -> list[int] | None:
        """
        Finds two numbers via nested loops. O(n^2) time complexity.
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n): # Start from i+1 to avoid using the same element twice
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
    ```
    *   **Time Complexity: O(n²)** - This is much slower. For a list of 10 numbers, you're doing close to 10 * 10 = 100 checks. For 1000 numbers, it's 1,000,000 checks. It gets very slow, very fast.
    *   **Space Complexity: O(1)** - This solution uses almost no extra memory, regardless of the input size.
*   **c. Trade-offs:** The brute-force method is often easier to think of and write on the spot. However, its poor time performance makes it impractical for large datasets, whereas the dictionary method remains fast.

## 7. Edge Cases
1.  **Negative Numbers:** What if `nums = [-3, 4, 3, 90]` and `target = 0`? The algorithm handles this perfectly. When it sees `-3`, it looks for `3`. When it sees `3`, it finds the `-3` in its memory and returns their indices `[0, 2]`.
2.  **Duplicate Numbers:** What if `nums = [5, 2, 5, 1]` and `target = 10`? The optimal solution will *not* work as written if it updates the index. But my implementation avoids this: it checks *before* writing. It sees the first `5` (index 0) and stores it. It sees `2`. It sees the second `5` (index 2), calculates `10 - 5 = 5`, finds `5` in the dictionary, and correctly returns `[0, 2]`.
3.  **No Solution:** The LeetCode problem guarantees a solution exists. But if it didn't (`nums = [1, 2, 3]`, `target = 7`), our function would finish the loop and return `None`, correctly indicating no pair was found.

## 8. Tiny Quiz
1.  In the optimal solution, why do we store the `number` as the key and the `index` as the value in the dictionary, and not the other way around?
2.  If `nums = [3, 3]` and `target = 6`, what would the optimal algorithm return?
3.  What is the main trade-off you make when choosing the optimal O(n) solution over the O(n²) brute-force one? 