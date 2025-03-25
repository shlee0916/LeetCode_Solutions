'''
https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/?envType=daily-question&envId=2025-03-25
'''

from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_range = []
        y_range = []
        for x1, y1, x2, y2 in rectangles:
            x_range.append([x1, x2])
            y_range.append([y1, y2])

        x_range.sort(key = lambda x: x[0])
        y_range.sort(key = lambda x: x[0])

        cnt_x = 0
        cnt_y = 0
        for idx in range(1, len(x_range)):
            if x_range[idx - 1][1] <= x_range[idx][0]:
                cnt_x += 1

            elif x_range[idx][1] < x_range[idx - 1][1]:
                x_range[idx][1] = x_range[idx - 1][1]
            
            if y_range[idx - 1][1] <= y_range[idx][0]:
                cnt_y += 1
            elif y_range[idx][1] < y_range[idx - 1][1]:
                y_range[idx][1] = y_range[idx - 1][1]

        return cnt_x >= 2 or cnt_y >= 2
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.checkValidCuts(n = 5, rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]])
    assert test1 == True

    test2 = sol.checkValidCuts(n = 4, rectangles = [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]])
    assert test2 == True

    test3 = sol.checkValidCuts(n = 4, rectangles = [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]])
    assert test3 == False
    