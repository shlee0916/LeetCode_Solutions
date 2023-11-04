'''
https://leetcode.com/problems/reachable-nodes-with-restrictions/description/
'''

from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = {edge: set() for edge in range(n)}

        for from_edge, to_edge in edges:
            graph[from_edge].add(to_edge)
            graph[to_edge].add(from_edge)
        
        stack = [0]
        visit = set(restricted)
        while stack:
            cur_node = stack.pop()
            visit.add(cur_node)
            for next_node in graph[cur_node]:
                if next_node not in visit:
                    stack.append(next_node)

        return len(visit) - len(restricted)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.reachableNodes(n = 7, edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], restricted = [4, 5])
    assert test1 == 4
    
    test2 = sol.reachableNodes(n = 7, edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], restricted = [4, 2, 1])
    assert test2 == 3
    