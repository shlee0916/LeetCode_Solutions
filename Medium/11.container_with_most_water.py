'''
https://leetcode.com/problems/container-with-most-water/
'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while (right - left) > 0:
            max_area = max(max_area, (right - left) * min(height[right], height[left]))
            
            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1
                
        return max_area
    
    
if __name__ == "__main__":
    sol = Solution()
    
    
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))