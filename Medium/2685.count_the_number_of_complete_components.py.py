'''
https://leetcode.com/problems/count-the-number-of-complete-components/
'''

from collections import defaultdict

from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        graph = defaultdict(list)

        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)

        seen = set()
        for start_edge in range(n):
            connected_cnt = 0

            if start_edge in seen:
                continue

            que = [start_edge]
            seen.add(start_edge)
            for edge_from in que:
                for edge_to in graph[edge_from]:
                    if edge_to not in seen:
                        connected_cnt += 1
                        que.append(edge_to)
                        seen.add(edge_to)

            if all(len(graph[edge_from]) == connected_cnt for edge_from in que):
                ans += 1

        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countCompleteComponents(n = 6, edges = [[0, 1], [0, 2], [1, 2], [3, 4]])
    assert test1 == 3
    
    test2 = sol.countCompleteComponents(n = 6, edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]])
    assert test2 == 1
    