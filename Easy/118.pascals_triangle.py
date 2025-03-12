'''
https://leetcode.com/problems/pascals-triangle/
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for row_idx in range(numRows):
            tmp_row = []
            for idx in range(row_idx + 1):
                if idx == 0 or idx == row_idx:
                    tmp_row.append(1)
                else:
                    tmp_row.append(tri[row_idx - 1][idx - 1] + tri[row_idx - 1][idx])
            tri.append(tmp_row)
                
        return tri
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.generate(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])