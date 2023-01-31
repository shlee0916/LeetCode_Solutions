'''
https://leetcode.com/problems/best-team-with-no-conflicts/description/
'''

from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        res = [0] * (max(ages) + 1)

        for score, age in sorted(zip(scores, ages)):
            res[age] = score + max(res[:age + 1])

        return max(res)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.bestTeamScore(scores = [1, 3, 5, 10, 15], ages = [1, 2, 3, 4, 5])
    print(test1, 34)
    assert test1 == 34

    test2 = sol.bestTeamScore(scores = [4, 5, 6, 5], ages = [2, 1, 2, 1])
    print(test2, 16)
    assert test2 == 16

    test3 = sol.bestTeamScore(scores = [1, 2, 3, 5], ages = [8, 9, 10, 1])
    print(test3, 6)
    assert test3 == 6
