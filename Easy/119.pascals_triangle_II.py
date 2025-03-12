'''
https://leetcode.com/problems/pascals-triangle-ii/
'''
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = []
        for row_idx in range(rowIndex + 1):
            tmp_row = []
            for idx in range(row_idx + 1):
                if idx == 0 or idx == row_idx:
                    tmp_row.append(1)
                else:
                    tmp_row.append(tri[row_idx - 1][idx - 1] + tri[row_idx - 1][idx])
            tri.append(tmp_row)
                
        return tri[rowIndex]


if __name__ == "__main__":
    sol = Solution()

    print(sol.getRow(2))