'''
https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/
'''

from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key = lambda x: -x[k])


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.sortTheStudents(score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], k = 2)
    assert test1 == [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]
    
    test2 = sol.sortTheStudents(score = [[3, 4], [5, 6]], k = 0)
    assert test2 == [[5, 6], [3, 4]]
    