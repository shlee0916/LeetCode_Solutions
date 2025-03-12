'''
https://leetcode.com/problems/unique-paths-ii/
'''
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        path_num_map = [0] * len(obstacleGrid[0])
        path_num_map[0] = 1
        for r_idx, row in enumerate(obstacleGrid):
            for c_idx, ob in enumerate(row):
                if ob == 1:
                    path_num_map[c_idx] = 0
                else:
                    if c_idx == 0:
                        path_num_map[c_idx] = 0 + path_num_map[c_idx]
                    else:
                        path_num_map[c_idx] = path_num_map[c_idx - 1] + path_num_map[c_idx]
                        
        return path_num_map[-1]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.uniquePathsWithObstacles([[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]), 0)