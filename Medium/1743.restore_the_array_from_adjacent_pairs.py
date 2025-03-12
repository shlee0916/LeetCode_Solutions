'''
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/?envType=daily-question&envId=2023-11-10
'''

from collections import defaultdict

from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for from_node, to_node in adjacentPairs:
            graph[from_node].append(to_node)
            graph[to_node].append(from_node)

        res = []
        seen = set()
        stack = [node for node in graph if len(graph[node]) == 1][1:]
        while stack:
            node = stack.pop()
            res.append(node)
            seen.add(node)
            for next_node in graph[node]:
                if next_node not in seen:
                    stack.append(next_node)

        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.restoreArray(adjacentPairs = [[2, 1], [3, 4], [3, 2]])
    assert test1 == [4, 3, 2, 1]

    test2 = sol.restoreArray(adjacentPairs = [[4, -2], [1, 4], [-3, 1]])
    assert test2 == [-3, 1, 4, -2]

    test3 = sol.restoreArray(adjacentPairs = [[100000, -100000]])
    assert test3 == [-100000, 100000]
