'''
https://leetcode.com/problems/find-if-path-exists-in-graph/description/
'''

from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {node: [] for node in range(n)}
        visit = set()

        for edge in edges:
            if edge[1] not in graph[edge[0]]:
                graph[edge[0]].append(edge[1])
            if edge[0] not in graph[edge[1]]:
                graph[edge[1]].append(edge[0])
        
        visit.add(source)
        stack = graph[source]
        stack.append(source)
        while stack:
            if destination in stack:
                return True

            node = stack.pop()
            if node not in visit:
                visit.add(node)
                stack.extend([new_node for new_node in graph[node] if new_node not in visit and new_node not in stack])

        return False
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.validPath(n = 3, edges = [[0, 1], [1, 2], [2, 0]], source = 0, destination = 2)
    print(test1, True)
    assert test1 == True
    
    test2 = sol.validPath(n = 6, edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source = 0, destination = 5)
    print(test2, False)
    assert test2 == False
    