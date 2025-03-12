'''
https://leetcode.com/problems/find-eventual-safe-states/description/
'''

from collections import defaultdict
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        state = defaultdict(lambda: "new")

        def dfs(node):
            state[node] = "unsafe"

            for next_node in graph[node]:
                if state[next_node] == "unsafe" or (state[next_node] == "new" and dfs(next_node)):
                    return True

            state[node] = "safe"

            return False

        res = []
        for node in range(len(graph)):
            if state[node] == "new":
                dfs(node)

            if state[node] == "safe":
                res.append(node)

        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.eventualSafeNodes(graph = [[1, 2], [2, 3], [5], [0], [5], [], []])
    assert test1 == [2, 4, 5, 6]
    
    test2 = sol.eventualSafeNodes(graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []])
    assert test2 == [4]
    