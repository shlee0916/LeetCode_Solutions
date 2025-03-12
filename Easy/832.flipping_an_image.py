'''
https://leetcode.com/problems/flipping-an-image/description/
'''

from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_img = []
        for row in image:
            new_row = []
            for value in row[::-1]:
                if value == 1:
                    new_row.append(0)
                else:
                    new_row.append(1)

            new_img.append(new_row)

        return new_img
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.flipAndInvertImage(image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]])
    assert test1 == [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    
    test2 = sol.flipAndInvertImage(image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])
    assert test2 == [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    