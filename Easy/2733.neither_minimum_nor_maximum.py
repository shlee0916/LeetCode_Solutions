'''
https://leetcode.com/problems/neither-minimum-nor-maximum/
'''

from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        nums.sort()

        return nums[1]
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findNonMinOrMax(nums = [3, 2, 1, 4])
    assert test1 == 2
    
    test2 = sol.findNonMinOrMax(nums = [1, 2])
    assert test2 == -1
    
    test3 = sol.findNonMinOrMax(nums = [2, 1, 3])
    assert test3 == 2
