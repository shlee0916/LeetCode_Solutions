'''
https://leetcode.com/problems/build-array-from-permutation/description/
'''

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[idx] for idx in nums]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.buildArray(nums = [0, 2, 1, 5, 3, 4])
    assert test1 == [0, 1, 2, 4, 5, 3]
    
    test2 = sol.buildArray(nums = [5, 0, 1, 2, 3, 4])
    assert test2 == [4, 5, 0, 1, 2, 3]
    