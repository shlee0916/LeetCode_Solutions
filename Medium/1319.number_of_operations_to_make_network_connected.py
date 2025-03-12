'''
https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
'''

from collections import defaultdict
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Recursive beats 37%
        # def dfs(com):
        #     visit.add(com)
        #     for conected_com in network[com]:
        #         if conected_com not in visit:
        #             dfs(conected_com)

        # Iterative, It's faster than recursive one, approximately 40ms. beats 67%
        def dfs(com):
            stack = [com]
            while stack:
                cur_com = stack.pop()
                if cur_com not in visit:
                    stack.extend(network[cur_com])
                    visit.add(cur_com)

        # Not enough cables
        if len(connections) < n - 1:
            return -1

        # Make network graph
        network = defaultdict(set)
        for con1, con2 in connections:
            network[con1].add(con2)
            network[con2].add(con1)

        # Find not connected
        visit = set()
        not_connected = 0
        for com in range(n):
            if com not in visit:
                not_connected += 1
                dfs(com)

        return not_connected - 1
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.makeConnected(n = 4, connections = [[0, 1], [0, 2], [1, 2]])
    print(test1, 1)
    assert test1 == 1

    test2 = sol.makeConnected(n = 6, connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]])
    print(test2, 2)
    assert test2 == 2

    test3 = sol.makeConnected(n = 6, connections = [[0, 1], [0, 2], [0, 3], [1, 2]])
    print(test3, -1)
    assert test3 == -1
    