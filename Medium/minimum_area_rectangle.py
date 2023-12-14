'''
https://leetcode.com/problems/minimum-area-rectangle/description/
'''

from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        points_set = set([tuple(point) for point in points])

        ans = float("inf")
        for x_idx, (x1, y1) in enumerate(points):
            for y_idx, (x2, y2) in enumerate(points[x_idx:], x_idx):
                if x2 > x1 and y2 > y1 and (x2, y1) in points_set and (x1, y2) in points_set:
                    ans = min(ans, (x2 - x1) * (y2 - y1))

        return ans if ans != float("inf") else 0


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minAreaRect(points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]])
    assert test1 == 4

    test2 = sol.minAreaRect(points = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]])
    assert test2 == 2
    