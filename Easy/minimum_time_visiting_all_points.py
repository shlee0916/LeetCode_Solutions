'''
https://leetcode.com/problems/minimum-time-visiting-all-points/?envType=daily-question&envId=2024-04-15
'''

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0

        x1, y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            ans += max(abs(x1 - x2), abs(y1 - y2))
            x1, y1 = x2, y2

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minTimeToVisitAllPoints(points = [[1, 1], [3, 4], [-1, 0]])
    assert test1 == 7
    
    test2 = sol.minTimeToVisitAllPoints(points = [[3, 2], [-2, 2]])
    assert test2 == 5
    