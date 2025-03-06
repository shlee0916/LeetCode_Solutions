'''
https://leetcode.com/problems/find-missing-and-repeated-values/?envType=daily-question&envId=2025-03-06
'''

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        num_map = [0] * len(grid) * len(grid)

        for row in grid:
            for num in row:
                num_map[num - 1] += 1


        ans = [-1, -1]
        for num, cnt in enumerate(num_map):
            if cnt == 2:
                ans[0] = num + 1
            
            if cnt == 0:
                ans[1] = num + 1

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findMissingAndRepeatedValues(grid = [[1, 3], [2, 2]])
    assert test1 == [2, 4]

    test2 = sol.findMissingAndRepeatedValues(grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]])
    assert test2 == [9, 5]
    