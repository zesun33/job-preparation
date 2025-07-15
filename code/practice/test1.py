from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sum = {0:1}
        for num in nums:
            current_sum += num
            diff = current_sum - k
            if diff in prefix_sum:
                count += prefix_sum[diff]
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return count


def main():
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))
    print(sol.subarraySum([1, 2, 3], 3))
    print(sol.subarraySum([1, -1, 0], 0))
    print(sol.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))


if __name__ == "__main__":
    main()
