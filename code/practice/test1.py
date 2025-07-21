class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_num_count = {}
        for num in nums:
            seen_num_count[num] = seen_num_count.get(num, 0) + 1
        return sorted(seen_num_count, key=seen_num_count.get, reverse=True)[:k]
