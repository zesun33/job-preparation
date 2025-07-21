from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements using a bucket sort approach.

        This method is optimal with O(n) time complexity because it avoids a
        comparison-based sort. Instead of sorting the numbers directly, it
        groups them by frequency into buckets.

        1.  **Count Frequencies (O(n)):** It iterates through the input `nums` once
            to build a hash map (`count`) storing `{number: frequency}`.
        2.  **Create Buckets (O(m)):** It iterates through the `m` unique numbers
            in the hash map and places each number into a "bucket" corresponding
            to its frequency. The bucket is a list of lists, where `buckets[i]`
            holds all numbers that appeared `i` times.
        3.  **Gather Results (O(m)):** It iterates backward from the highest-frequency
            bucket to collect elements until `k` elements are found.

        The variable `res` is a common convention for the "result" list being built.
        """
        # Step 1: Count frequency of each number.
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Create frequency buckets.
        # The list of buckets, where index is the frequency. The size must be
        # `len(nums) + 1` to handle the edge case where one number appears
        # `len(nums)` times, requiring an index of `len(nums)`.
        freq_buckets = [[] for i in range(len(nums) + 1)]

        # Populate the buckets.
        for n, c in count.items():
            freq_buckets[c].append(n)

        # Step 3: Gather the top k results.
        res = []
        # Iterate from the highest possible frequency down to 1.
        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements using a simpler, sort-based approach.
        This is more concise but less performant for very large inputs.

        - Time Complexity: O(n log n) due to the sorting step.
        - Space Complexity: O(n) to store the frequency counter.
        """
        # Use collections.Counter as a shortcut to build the frequency map.
        count = collections.Counter(nums)

        # `sorted()` creates a new list.
        # `key=count.get` tells sorted() to use the dictionary's values (the frequencies)
        # as the basis for comparison instead of the keys (the numbers).
        return sorted(count, key=count.get, reverse=True)[:k]

# Comprehensive Test Cases
if __name__ == '__main__':
    solver = Solution()
    test_cases = [
        ("Standard case", [1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ("Only one element", [1], 1, [1]),
        ("Negative numbers", [4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
        ("All elements are the same", [5, 5, 5, 5], 1, [5]),
        ("k equals unique elements", [1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ("Tie in frequency", [6, 6, 7, 7, 8, 8], 2, [6, 7, 8]), # Expected can be any 2
    ]

    for i, (name, nums, k, expected) in enumerate(test_cases):
        print(f"--- Test Case {i+1}: {name} ---")
        print(f"nums = {nums}, k = {k}")

        # Test the optimal O(n) bucket sort solution
        result_optimal = solver.topKFrequent(nums, k)
        print(f"Optimal Result: {result_optimal}")
        
        # Test the O(n log n) sort-based solution
        result_sort = solver.topKFrequent_sort(nums, k)
        print(f"Sort-Based Result: {result_sort}")

        # Assertions
        if name == "Tie in frequency":
            assert len(result_optimal) == k
            assert all(item in expected for item in result_optimal)
            assert len(result_sort) == k
            assert all(item in expected for item in result_sort)
        else:
            assert sorted(result_optimal) == sorted(expected)
            assert sorted(result_sort) == sorted(expected)
        
        print("Both solutions passed!\n")

    print("All test cases passed!")