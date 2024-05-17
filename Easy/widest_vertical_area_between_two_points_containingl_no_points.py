'''
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/?envType=daily-question&envId=2024-05-17
'''

from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])

        max_width = 0
        pre = points[0][0]
        for x, _ in points[1:]:
            max_width = max(max_width, x - pre)
            pre = x

        return max_width


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxWidthOfVerticalArea(points = [[8, 7], [9, 9], [7, 4], [9, 7]])
    assert test1 == 1
    
    test2 = sol.maxWidthOfVerticalArea(points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]])
    assert test2 == 3
    