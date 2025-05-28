'''
https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description/?envType=daily-question&envId=2025-05-28
'''

from typing import List


class Solution:
    def create_tree(self, edges):
        graph = [[] for _ in range(len(edges) + 1)]

        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)

        return graph


    def dfs(self, tree, k):
        cnts = [0] * len(tree)
        for root in range(len(tree)):
            stack = [(root, -1, 0)]
            while stack:
                cur_node, parent, depth = stack.pop()

                if depth <= k:
                    cnts[root] += 1

                for next_node in tree[cur_node]:
                    if next_node != parent:
                        stack.append((next_node, cur_node, depth + 1))

        return cnts


    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        tree1 = self.create_tree(edges1)
        tree2 = self.create_tree(edges2)

        tree2_max = max(self.dfs(tree2, k - 1))
   
        return [cnt + tree2_max for cnt in self.dfs(tree1, k)]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxTargetNodes(edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]], edges2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], k = 2)
    assert test1 == [9, 7, 9, 8, 8]
    
    test2 = sol.maxTargetNodes(edges1 = [[0, 1], [0, 2], [0, 3], [0, 4]], edges2 = [[0, 1], [1, 2], [2, 3]], k = 1)
    assert test2 == [6, 3, 3, 3, 3]
    