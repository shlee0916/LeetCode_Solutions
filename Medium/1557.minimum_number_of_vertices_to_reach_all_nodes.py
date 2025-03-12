'''
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/
'''

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = set(range(n))
        all_incoming_nodes = set([arrive for depart, arrive in edges])
        
        return result - all_incoming_nodes
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findSmallestSetOfVertices(n = 6, edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]])
    assert set(test1) == set([0, 3])

    test2 = sol.findSmallestSetOfVertices(n = 5, edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]])
    assert set(test2) == set([0, 2, 3])
