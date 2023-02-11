'''
https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
'''

from collections import defaultdict

from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red, blue = 0, 1
        graph = {0: defaultdict(list), 1: defaultdict(list)}

        for depart, arrival in redEdges:
            graph[red][depart].append((arrival, red))
        for depart, arrival in blueEdges:
            graph[blue][depart].append((arrival, blue))

        res = [float("inf")] * n

        que = [(0, red), (0, blue)]
        visit = {0: set(), 1: set()}
        path_len = -1
        while que:
            path_len += 1
            cur_level_len = len(que)
            for _ in range(cur_level_len):
                node, color = que.pop(0)

                opp_color = 1 - color
                res[node] = min(path_len, res[node])

                next_nodes = graph[opp_color][node]
                for next_node, color in next_nodes:
                    if next_node not in visit[opp_color]:
                        visit[opp_color].add(next_node)
                        que.append((next_node, opp_color))

        return [num if num != float("inf") else -1 for num in res]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.shortestAlternatingPaths(n = 3, redEdges = [[0, 1], [1, 2]], blueEdges = [])
    print(test1, [0, 1, -1])
    assert test1 == [0, 1, -1]
    
    test2 = sol.shortestAlternatingPaths(n = 3, redEdges = [[0, 1]], blueEdges = [[2, 1]])
    print(test2, [0, 1, -1])
    assert test2 == [0, 1, -1]
    