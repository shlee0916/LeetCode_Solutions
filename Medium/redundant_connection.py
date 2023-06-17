'''
https://leetcode.com/problems/redundant-connection/description/
'''

from typing import List


class UnionFind:
    def __init__(self, length):
        self.parents = [idx for idx in range(length)]
        self.size = [1] * length

    
    def find(self, child):
        if child != self.parents[child]:
            self.parents[child] = self.find(self.parents[child])
        return self.parents[child]


    def union(self, u, v):
        u_parent, v_parent = self.find(u), self.find(v)
        if u_parent == v_parent:
            return False

        if self.size[u_parent] > self.size[v_parent]:
            self.size[u_parent] += self.size[v_parent]
            self.parents[v_parent] = u_parent
        else:
            self.size[v_parent] += self.size[u_parent]
            self.parents[u_parent] = v_parent

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        length = len(edges)
        union_find = UnionFind(length)

        for u, v in edges:
            if not union_find.union(u - 1, v - 1):
                return [u, v]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findRedundantConnection(edges = [[1, 2], [1, 3], [2, 3]])
    assert test1 == [2, 3]
    
    test2 = sol.findRedundantConnection(edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
    assert test2 == [1, 4]
    