'''
https://leetcode.com/problems/rotating-the-box/description/
'''

from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        row_limit = len(box[0]) - 1
        for row in box:
            position = row_limit
            for target_idx in range(row_limit, -1, -1):
                if row[target_idx] == "*":
                    position = target_idx - 1
                elif row[target_idx] == "#":
                    row[target_idx], row[position] = row[position], row[target_idx]
                    position -= 1

        return zip(*box[::-1])


if __name__ == "__main__":
    def zip2list(matrix: zip): # Test helper
        return [list(row) for row in matrix]

    sol = Solution()

    test1 = sol.rotateTheBox(box = [["#", ".", "#"]])
    assert zip2list(test1) == [["."],
                               ["#"],
                               ["#"]]
    
    test2 = sol.rotateTheBox(box = [["#", ".", "*", "."], 
                                    ["#", "#", "*", "."]])
    assert zip2list(test2) == [["#", "."],
                               ["#", "#"],
                               ["*", "*"],
                               [".", "."]]
    
    test3 = sol.rotateTheBox(box = [["#", "#", "*", ".", "*", "."], 
                                    ["#", "#", "#", "*", ".", "."], 
                                    ["#", "#", "#", ".", "#", "."]])
    assert zip2list(test3) == [[".", "#", "#"], 
                     [".", "#", "#"], 
                     ["#", "#", "*"], 
                     ["#", "*", "."], 
                     ["#", ".", "*"], 
                     ["#", ".", "."]]
    