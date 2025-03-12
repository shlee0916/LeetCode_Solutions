'''
https://leetcode.com/problems/binary-subarrays-with-sum/?envType=daily-question&envId=2024-03-14
'''

from collections import Counter

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_map = Counter({0: 1})
        ans = 0
        prefix = 0

        for num in nums:
            prefix += num
            ans += prefix_map[prefix - goal]
            prefix_map[prefix] += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numSubarraysWithSum(nums = [1, 0, 1, 0, 1], goal = 2)
    assert test1 == 4

    test2 = sol.numSubarraysWithSum(nums = [0, 0, 0, 0, 0], goal = 0)
    assert test2 == 15
    