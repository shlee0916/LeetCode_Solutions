'''
https://leetcode.com/problems/find-all-groups-of-farmland/description/
'''

from typing import List, Tuple


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        row_limit = len(land)
        col_limit = len(land[0])

        def dfs(row: int, col: int) -> Tuple[int, int]:
            coord = (0, 0)
            if 0 <= row < row_limit and 0 <= col < col_limit and land[row][col] != 0:
                land[row][col] = 0

                row1, col1 = dfs(row + 1, col)
                row2, col2 = dfs(row, col + 1)

                max_row = max(row1, row2, row)
                max_col = max(col1, col2, col)

                coord = (max_row, max_col)
            
            return coord

        for r_idx in range(row_limit):
            for c_idx in range(col_limit):
                if land[r_idx][c_idx] == 1:
                    r_end, c_end = dfs(r_idx, c_idx)
                    ans.append([r_idx, c_idx, r_end, c_end])

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findFarmland(land = [[1, 0, 0], [0, 1, 1], [0, 1, 1]])
    assert test1 == [[0, 0, 0, 0], [1, 1, 2, 2]]

    test2 = sol.findFarmland(land = [[1, 1], [1, 1]])
    assert test2 == [[0, 0, 1, 1]]
    