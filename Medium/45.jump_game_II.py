'''
https://leetcode.com/problems/jump-game-ii/
'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        left, right = 0, nums[0]
        times = 1
        while right < len(nums) - 1:
            times += 1
            next = max(i + nums[i] for i in range(left, right + 1))
            left, right = right, next
        
        return times
    

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.jump([2, 3, 1, 1, 4]), 2)
    print(sol.jump([2, 3, 0, 1, 4]), 2)