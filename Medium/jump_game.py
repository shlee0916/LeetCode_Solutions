'''
https://leetcode.com/problems/jump-game/
'''
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_idx = 0
        max_idx = nums[0]
        
        if max_idx + 1 >= len(nums):
            return True
        
        while cur_idx < max_idx:
            cur_idx += 1
            
            max_idx = max(max_idx, cur_idx + nums[cur_idx])
            if max_idx + 1 >= len(nums):
                return True
            
        return False
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.canJump([2, 3, 1, 1, 4]), True)
    print(sol.canJump([3, 2, 1, 0, 4]), False)