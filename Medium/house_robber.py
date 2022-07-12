'''
https://leetcode.com/problems/house-robber/
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_a, rob_b = 0, 0
        for num in nums:
            rob_a, rob_b = rob_b, max(rob_a + num, rob_b)
            
        return rob_b
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.rob([2, 1, 1, 2]), 4)