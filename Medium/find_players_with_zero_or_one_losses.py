'''
https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
'''

from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        teams = {}

        for winner, loser in matches:
            if winner not in teams.keys():
                teams[winner] = [0, 0]
            if loser not in teams.keys():
                teams[loser] = [0, 0]

            teams[winner][0] += 1
            teams[loser][1] += 1

        winners = [key for key, value in teams.items() if value[1] == 0]
        losers = [key for key, value in teams.items() if value[1] == 1]

        winners.sort()
        losers.sort()

        return [winners, losers]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]])
    print(test1, [[1, 2, 10], [4, 5, 7, 8]])
    assert test1 == [[1, 2, 10], [4, 5, 7, 8]]

    test2 = sol.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]])
    print(test2, [[1, 2, 5, 6], []])
    assert test2 == [[1, 2, 5, 6], []]
