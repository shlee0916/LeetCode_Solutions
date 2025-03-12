'''
https://leetcode.com/problems/sum-of-distances-in-tree/description/
'''

from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(root, pre):
            for node in graph[root]:
                if node != pre:
                    dfs(node, root)
                    cnt[root] += cnt[node]
                    ans[root] += cnt[node] + ans[node]


        def dfs2(root, pre):
            for node in graph[root]:
                if node != pre:
                    ans[node] = ans[root] - cnt[node] + n - cnt[node]
                    dfs2(node, root)


        graph = {node: set() for node in range(n)}
        ans = [0] * n
        cnt = [1] * n

        for l_node, r_node in edges:
            graph[l_node].add(r_node)
            graph[r_node].add(l_node)

        dfs(0, -1)
        dfs2(0, -1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.sumOfDistancesInTree(n = 6, edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]])
    print(test1, [8, 12, 6, 10, 10, 10])
    assert test1 == [8, 12, 6, 10, 10, 10]
    
    test2 = sol.sumOfDistancesInTree(n = 1, edges = [])
    print(test2, [0])
    assert test2 == [0]
    
    test3 = sol.sumOfDistancesInTree(n = 2, edges = [[1, 0]])
    print(test3, [1, 1])
    assert test3 == [1, 1]
