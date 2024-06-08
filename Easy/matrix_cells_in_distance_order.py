'''
https://leetcode.com/problems/matrix-cells-in-distance-order/description/
'''

from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ans = []
        for row in range(rows):
            for col in range(cols):
                ans.append([row, col])

        return sorted(ans, key = lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0)
    assert test1 == [[0, 0], [0, 1]]

    test2 = sol.allCellsDistOrder(rows = 2, cols = 2, rCenter = 0, cCenter = 1)
    assert test2 == [[0, 1], [0, 0], [1, 1], [1, 0]]

    test3 = sol.allCellsDistOrder(rows = 2, cols = 3, rCenter = 1, cCenter = 2)
    assert test3 == [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]
