'''
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/
'''

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total_pair_sum = [nums[idx] + nums[-idx - 1] for idx in range(len(nums) // 2)]

        return max(total_pair_sum)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minPairSum(nums = [3, 5, 2, 3])
    assert test1 == 7
    
    test2 = sol.minPairSum(nums = [3, 5, 4, 2, 4, 6])
    assert test2 == 8
    