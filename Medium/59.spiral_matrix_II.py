'''
https://leetcode.com/problems/spiral-matrix-ii/
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        
        num = 1
        top, bot = 0, n - 1
        while num <= n ** 2:
            # up edge
            for idx in range(top, bot + 1):
                mat[top][idx] = num
                num += 1
            
            # right edge
            for idx in range(top + 1, bot + 1):
                mat[idx][bot] = num
                num += 1
                
            # down edge
            for idx in range(top, bot)[::-1]:
                mat[bot][idx] = num
                num += 1
                
            # left edge
            for idx in range(top + 1, bot)[::-1]:
                mat[idx][top] = num
                num += 1
                
            top += 1
            bot -= 1
            
        return mat
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.generateMatrix(3))