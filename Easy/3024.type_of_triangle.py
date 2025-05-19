'''
https://leetcode.com/problems/type-of-triangle/description/?envType=daily-question&envId=2025-05-19
'''

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        longest = max(nums)

        if not sum(nums) - longest > longest:
            return "none"

        if len(set(nums)) == 1:
            return "equilateral"
        elif len(set(nums)) == 2:
            return "isosceles"
        else:
            return "scalene"
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.triangleType(nums = [3, 3, 3])
    assert test1 == "equilateral"
    
    test2 = sol.triangleType(nums = [3, 4, 5])
    assert test2 == "scalene"
    