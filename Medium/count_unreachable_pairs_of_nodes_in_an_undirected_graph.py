'''
https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
'''

from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for begin, end in edges:
            graph[begin].append(end)
            graph[end].append(begin)

        groups = []
        visit = set()
        for node in range(n):
            if node not in visit:
                stack = [node]
                group_size = 0
                while stack:
                    cur_node = stack.pop()
                    if cur_node not in visit:
                        visit.add(cur_node)
                        stack.extend(graph[cur_node])
                        group_size += 1

                groups.append(group_size)

        res = 0
        for size in groups:
            res += (n - size) * size

        return res // 2


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countPairs(n = 3, edges = [[0, 1], [0, 2], [1, 2]])
    print(test1, 0)
    assert test1 == 0
    
    test2 = sol.countPairs(n = 7, edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]])
    print(test2, 14)
    assert test2 == 14
    