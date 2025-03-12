'''
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
'''

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) < 1:
            return 0

        nums.sort()
        ans = nums[k - 1] - nums[0]
        for idx in range(k, len(nums)):
            ans = min(ans, nums[idx] - nums[idx - k + 1])

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minimumDifference(nums = [90], k = 1)
    assert test1 == 0
    
    test2 = sol.minimumDifference(nums = [9, 4, 1, 7], k = 2)
    assert test2 == 2
    