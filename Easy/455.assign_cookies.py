'''
https://leetcode.com/problems/assign-cookies/
'''
from typing import List
import bisect


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        for cookie in s:
            if bisect.bisect_right(g, cookie) > result:
                result += 1
                
        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.findContentChildren([1, 2, 3], [1, 1]), 1)