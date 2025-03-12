'''
https://leetcode.com/problems/maximum-total-importance-of-roads/?envType=daily-question&envId=2024-06-28
'''

from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        degrees = [[0, idx] for idx in range(n)]

        for from_node, to_node in roads:
            degrees[from_node][0] += 1
            degrees[to_node][0] += 1

        degrees.sort(key = lambda node: node[0], reverse = True)
        for idx, (degree, node) in enumerate(degrees):
            ans += degree * (len(degrees) - idx)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumImportance(n = 5, roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])
    assert test1 == 43

    test2 = sol.maximumImportance(n = 5, roads = [[0, 3], [2, 4], [1, 3]])
    assert test2 == 20
    