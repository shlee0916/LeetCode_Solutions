'''
https://leetcode.com/problems/most-profitable-path-in-a-tree/?envType=daily-question&envId=2025-02-24
'''

from collections import defaultdict

from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        bob_time = [-1] * len(amount)
        visit = set()
        def bob_dfs(node, time):
            bob_time[node] = time
            visit.add(node)

            if node == 0:
                return True

            for next_node in graph[node]:
                if next_node not in visit:
                    if bob_dfs(next_node, time + 1):
                        return True

            bob_time[node] = -1

            return False
        
        bob_dfs(bob, 0)

        alice_cost = float("-inf")
        visit = set()
        stack = [(0, 0, 0)] # node, cost, time
        while stack:
            cur_node, cur_cost, cur_time = stack.pop()
            visit.add(cur_node)

            if bob_time[cur_node] == -1 or cur_time < bob_time[cur_node]:
                cur_cost += amount[cur_node]
            elif cur_time == bob_time[cur_node]:
                cur_cost += amount[cur_node] // 2

            if len(graph[cur_node]) == 1 and cur_node != 0:
                alice_cost = max(alice_cost, cur_cost)

            for next_node in graph[cur_node]:
                if next_node not in visit:
                    stack.append((next_node, cur_cost, cur_time + 1))
            
        return alice_cost


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.mostProfitablePath(edges = [[0, 1], [1, 2], [1, 3], [3, 4]], bob = 3, amount = [-2, 4, 2, -4, 6])
    assert test1 == 6

    test2 = sol.mostProfitablePath(edges = [[0, 1]], bob = 1, amount = [-7280, 2350])
    assert test2 == -7280
    