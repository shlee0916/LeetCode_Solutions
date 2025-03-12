'''
https://leetcode.com/problems/subrectangle-queries/
'''

from copy import deepcopy

from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self._rectangle = deepcopy(rectangle)
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row_idx in range(row1, row2 + 1):
            for col_idx in range(col1, col2 + 1):
                self._rectangle[row_idx][col_idx] = newValue
    

    def getValue(self, row: int, col: int) -> int:
        return self._rectangle[row][col]
        

if __name__ == "__main__":
    sq = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])

    assert sq.getValue(0, 2) == 1
    
    sq.updateSubrectangle(0, 0, 3, 2, 5)
    
    assert sq.getValue(0, 2) == 5
    assert sq.getValue(3, 1) == 5
    

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)