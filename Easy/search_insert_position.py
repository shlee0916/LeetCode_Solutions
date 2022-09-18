'''
https://leetcode.com/problems/search-insert-position/
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0: return None
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + ((right - left) // 2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        return left + 1 if nums[left] < target else left
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.searchInsert([1, 3, 5, 6], 5), 2)
    print(sol.searchInsert([1, 3, 5, 6], 2), 1)
    print(sol.searchInsert([1, 3, 5, 6], 7), 4)