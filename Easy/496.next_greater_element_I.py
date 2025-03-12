'''
https://leetcode.com/problems/next-greater-element-i/
'''
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        map = {}
        
        for n in nums2:
            while stack and n > stack[-1]:
                map[stack.pop()] = n
            stack.append(n)
            
        return [map.get(n, -1) for n in nums1]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])