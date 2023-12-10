'''
https://leetcode.com/problems/transpose-matrix/description/?envType=daily-question&envId=2023-12-10
'''

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.transpose(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert test1 == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    test2 = sol.transpose(matrix = [[1, 2, 3], [4, 5, 6]])
    assert test2 == [[1, 4], [2, 5], [3, 6]]
    