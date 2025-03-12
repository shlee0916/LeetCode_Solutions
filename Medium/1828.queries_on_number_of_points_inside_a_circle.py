'''
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/description/
'''

from math import sqrt

from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for query_x, query_y, query_r in queries:
            count = 0
            for point_x, point_y in points:
                if sqrt((query_x - point_x) ** 2 + (query_y - point_y) ** 2) <= query_r:
                    count += 1

            ans.append(count)

        return ans 
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countPoints(points = [[1, 3], [3, 3], [5, 3], [2, 2]], queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]])
    assert test1 == [3, 2, 2]

    test2 = sol.countPoints(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]])
    assert test2 == [2, 3, 2, 4]
