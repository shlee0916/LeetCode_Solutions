'''
https://leetcode.com/problems/longest-square-streak-in-an-array/?envType=daily-question&envId=2024-10-28
'''

from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nums_set = set(nums)
        
        ans = 0
        for num in nums:
            cur_len = 0

            cur = num 
            while cur in nums_set:
                cur_len += 1
                cur = cur ** 2

            if cur_len > 1:
                ans = max(ans, cur_len)
        
        return ans if ans > 1 else -1

        
if __name__ == "__main__":
    sol = Solution()

    test1 = sol.longestSquareStreak(nums = [4, 3, 6, 16, 8, 2])
    assert test1 == 3

    test2 = sol.longestSquareStreak(nums = [2, 3, 5, 6, 7])
    assert test2 == -1
    