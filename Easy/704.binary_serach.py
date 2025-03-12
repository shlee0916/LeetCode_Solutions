'''
https://leetcode.com/problems/binary-search/description/
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums)
        
        while begin < end:
            mid = ((end - begin) // 2) + begin
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                begin = mid + 1
            elif nums[mid] > target:
                end = mid
                
        return -1
    

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.search([-1, 0, 3, 5, 9], 3))
    print(sol.search([-1, 0, 3, 5, 9], -2))
    print(sol.search([-1, 0, 3, 5, 9], 9))