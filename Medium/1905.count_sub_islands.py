'''
https://leetcode.com/problems/count-sub-islands/description/
'''

from typing import List


class Solution:
    def find_all_island(self, matrix: List[List[int]]):
            islands = []
            row_len = len(matrix)
            col_len = len(matrix[0])

            visit = set()
            for row_idx in range(row_len):
                for col_idx in range(col_len):
                    if matrix[row_idx][col_idx] == 1 and (row_idx, col_idx) not in visit:
                        cur_island = [(row_idx, col_idx)]
                        stack = [(row_idx, col_idx)]
                        while stack:
                            cur_x, cur_y = stack.pop()

                            for new_x, new_y in ((cur_x + 1, cur_y), 
                                                (cur_x - 1, cur_y), 
                                                (cur_x, cur_y + 1), 
                                                (cur_x, cur_y - 1)):
                                if 0 <= new_x < row_len and 0 <= new_y < col_len:
                                    if matrix[new_x][new_y] == 1 and (new_x, new_y) not in visit:
                                        stack.append((new_x, new_y))
                                        visit.add((new_x, new_y))
                                        cur_island.append((new_x, new_y))

                        islands.append(cur_island)

            return islands


    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        grid2_island = self.find_all_island(grid2)

        cnt = 0
        for island in grid2_island:
            if all(True if grid1[x][y] else False for x, y in island):
                cnt += 1

        return cnt


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countSubIslands(grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],  grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]])
    assert test1 == 3
    
    test2 = sol.countSubIslands(grid1 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],  grid2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]])
    assert test2 == 2
    