'''
https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
'''

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0
        left = 0
        right = 1
        while left < len(nums) - 2:
            if right > len(nums) - 1:
                left += 1
                right = left + 1
            
            if nums[left] + nums[right] < target:
                ans += 1
            right += 1

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countPairs(nums = [-1, 1, 2, 3, 1], target = 2)
    assert test1 == 3
    
    test2 = sol.countPairs(nums = [-6, 2, 5, -2, -7, -1, 3], target = -2)
    assert test2 == 10
    