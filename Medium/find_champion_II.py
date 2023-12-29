'''
https://leetcode.com/problems/find-champion-ii/description/
'''

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return (n == 1) - 1

        _, weak_teams = zip(*edges)
        strong_team = set(range(n)) - set(weak_teams)

        return strong_team.pop() if len(strong_team) == 1 else - 1
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findChampion(n = 3, edges = [[0, 1], [1, 2]])
    assert test1 == 0

    test2 = sol.findChampion(n = 4, edges = [[0, 2], [1, 3], [1, 2]])
    assert test2 == -1
    