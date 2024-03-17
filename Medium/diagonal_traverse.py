'''
https://leetcode.com/problems/diagonal-traverse/
'''

from collections import defaultdict

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_limit = len(mat)
        col_limit = len(mat[0])

        traversal = defaultdict(list)
        for row in range(row_limit):
            for col in range(col_limit):
                traversal[row + col].append(mat[row][col])
        
        ans = []
        for row_col, vals in traversal.items():
            if row_col % 2 == 0:
                ans.extend(vals[::-1])
            else:
                ans.extend(vals)

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findDiagonalOrder(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert test1 == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    
    test2 = sol.findDiagonalOrder(mat = [[1, 2], [3, 4]])
    assert test2 == [1, 2, 3, 4]
    