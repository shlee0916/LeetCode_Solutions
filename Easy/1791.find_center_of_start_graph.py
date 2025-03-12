'''
https://leetcode.com/problems/find-center-of-star-graph/description/
'''

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
            return (set(edges[0]) & set(edges[1])).pop()


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findCenter(edges = [[1, 2], [2, 3], [4, 2]])
    assert test1 == 2
    
    test2 = sol.findCenter(edges = [[1, 2], [5, 1], [1, 3], [1, 4]])
    assert test2 == 1
    