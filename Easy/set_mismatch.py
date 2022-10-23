'''
https://leetcode.com/problems/set-mismatch/
'''
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = len(nums) * (len(nums) + 1) // 2
        
        missing = total - sum(set(nums))
        duplicate = sum(nums) + missing - total
        
        return [duplicate, missing]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.findErrorNums([1, 2, 2, 4]), [2, 3])
    print(sol.findErrorNums([1, 1]), [1, 2])