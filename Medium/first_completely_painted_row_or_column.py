'''
https://leetcode.com/problems/first-completely-painted-row-or-column/?envType=daily-question&envId=2025-01-20
'''

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = [len(mat[0])] * len(mat)
        cols = [len(mat)] * len(mat[0])

        nums_meta = {}
        for r_idx, row in enumerate(mat):
            for c_idx, num in enumerate(row):
                nums_meta[num] = (r_idx, c_idx)

        for idx, num in enumerate(arr):
            r_idx, c_idx = nums_meta[num]
            rows[r_idx] -= 1
            cols[c_idx] -= 1

            if rows[r_idx] == 0 or cols[c_idx] == 0:
                return idx

        return idx
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.firstCompleteIndex(arr = [1, 3, 4, 2], mat = [[1, 4], [2, 3]])
    assert test1 == 2

    test2 = sol.firstCompleteIndex(arr = [2, 8, 7, 4, 1, 3, 5, 6, 9], mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]])
    assert test2 == 3
