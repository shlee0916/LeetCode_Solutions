'''
https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/description/
'''

from collections import deque

from typing import List


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        row_limit = len(grid)
        col_limit = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        que = deque([(0, grid[start[0]][start[1]], start[0], start[1])])
        visited = set([(start[0], start[1])])
        ans_cand = []
        while que:
            dist, price, row, col = que.popleft()

            if pricing[0] <= price <= pricing[1]:
                ans_cand.append((dist, price, row, col))

            for row_delta, col_delta in directions:
                new_row = row + row_delta
                new_col = col + col_delta

                if 0 <= new_row < row_limit and 0 <= new_col < col_limit:
                    if (new_row, new_col) not in visited and grid[new_row][new_col] != 0:
                        visited.add((new_row, new_col))
                        que.append((dist + 1, grid[new_row][new_col], new_row, new_col))

        ans_cand.sort()

        return [[row, col] for _, _, row, col in ans_cand[:k]]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.highestRankedKItems(grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3)
    assert test1 == [[0,1],[1,1],[2,1]]
    
    test2 = sol.highestRankedKItems(grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2)
    assert test2 == [[2,1],[1,2]]
    
    test3 = sol.highestRankedKItems(grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3)
    assert test3 == [[2,1],[2,0]]
    