'''
https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
'''

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]

        for x, y in coordinates[2:]:
            if (y - y1) * (x - x2) != (y - y2) * (x - x1):
                return False

        return True
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.checkStraightLine(coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    assert test1 == True

    test2 = sol.checkStraightLine(coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
    assert test2 == False
    