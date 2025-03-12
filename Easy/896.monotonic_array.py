'''
https://leetcode.com/problems/monotonic-array/description/?envType=daily-question&envId=2023-09-29
'''

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sorted_arr = sorted(nums)
        rev_sorted_arr = sorted(nums, reverse = True)

        return nums == sorted_arr or nums == rev_sorted_arr
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isMonotonic(nums = [1,2,2,3])
    assert test1 == True
    
    test2 = sol.isMonotonic(nums = [6,5,4,4])
    assert test2 == True
    
    test3 = sol.isMonotonic(nums = [1,3,2])
    assert test3 == False
    