'''
https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/?envType=daily-question&envId=2025-04-09
'''

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1

        ans = 0
        num_set = set(nums)
        for num in num_set:
            if num > k:
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minOperations(nums = [5, 2, 5, 4, 5], k = 2)
    assert test1 == 2

    test2 = sol.minOperations(nums = [2, 1, 2], k = 2)
    assert test2 == -1

    test3 = sol.minOperations(nums = [9, 7, 5, 3], k = 1)
    assert test3 == 4
    