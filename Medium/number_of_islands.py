'''
https://leetcode.com/problems/number-of-islands/
'''
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        island_cnt = 0
        land_stack = []
        for r_idx in range(len(grid)):
            for c_idx in range(len(grid[r_idx])):
                # print(r_idx, c_idx)
                # if visit[r_idx][c_idx] == 0:
                    # visit[r_idx][c_idx] = 1

                if grid[r_idx][c_idx] == "1" and visit[r_idx][c_idx] != 1:
                    land_stack.append((r_idx, c_idx))
                    while land_stack:
                        cur_pos = land_stack.pop()
                        visit[cur_pos[0]][cur_pos[1]] = 1

                        if cur_pos[1] + 1 < len(grid[cur_pos[0]]) and grid[cur_pos[0]][cur_pos[1] + 1] == "1" and visit[cur_pos[0]][cur_pos[1] + 1] == 0:
                            land_stack.append((cur_pos[0], cur_pos[1] + 1))
                        if cur_pos[1] - 1 >= 0 and grid[cur_pos[0]][cur_pos[1] - 1] == "1" and visit[cur_pos[0]][cur_pos[1] - 1] == 0:
                            land_stack.append((cur_pos[0], cur_pos[1] - 1))
                        if cur_pos[0] + 1 < len(grid) and grid[cur_pos[0] + 1][cur_pos[1]] == "1" and visit[cur_pos[0] + 1][cur_pos[1]] == 0:
                            land_stack.append((cur_pos[0] + 1, cur_pos[1]))
                        if cur_pos[0] - 1 >= 0 and grid[cur_pos[0] - 1][cur_pos[1]] == "1" and visit[cur_pos[0] - 1][cur_pos[1]] == 0:
                            land_stack.append((cur_pos[0] - 1, cur_pos[1]))

                    island_cnt += 1
                    
        return island_cnt
    
    
if __name__ == "__main__":
    sol = Solution()
    
    grid1 = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
    
    grid2 = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
    
    grid3 = [
            ["1","1","1"],
            ["0","1","0"],
            ["1","1","1"]
            ]
    
    print(sol.numIslands(grid1), 1)
    print(sol.numIslands(grid2), 3)
    print(sol.numIslands(grid3), 1)