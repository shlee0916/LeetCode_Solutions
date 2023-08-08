'''
https://leetcode.com/problems/row-with-maximum-ones/description/
'''

from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]

        for r_idx, row in enumerate(mat):
            if row.count(1) > ans[1]:
                ans[0] = r_idx
                ans[1] = row.count(1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.rowAndMaximumOnes(mat = [[0, 1], [1, 0]])
    assert test1 == [0, 1]
    
    test2 = sol.rowAndMaximumOnes(mat = [[0, 0, 0], [0, 1, 1]])
    assert test2 == [1, 2]
    
    test3 = sol.rowAndMaximumOnes(mat = [[0, 0], [1, 1], [0, 0]])
    assert test3 == [1, 2]
    