'''
https://leetcode.com/problems/array-partition/
'''
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.arrayPairSum([1, 4, 3, 2]), 4)
    print(sol.arrayPairSum([6,2,6,5,1,2]), 9)