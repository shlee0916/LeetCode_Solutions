'''
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
'''

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cur_length = 1
        max_length = 1

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                cur_length += 1
            else:
                max_length = max(cur_length, max_length)
                cur_length = 1

        return max(cur_length, max_length)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findLengthOfLCIS(nums = [1, 3, 5, 4, 7])
    assert test1 == 3
    
    test2 = sol.findLengthOfLCIS(nums = [2, 2, 2, 2, 2])
    assert test2 == 1
    