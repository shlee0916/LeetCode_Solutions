'''
https://leetcode.com/problems/find-missing-observations/?envType=daily-question&envId=2024-09-05
'''

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = len(rolls) + n
        n_sum = (mean * total) - sum(rolls)

        if n_sum / n > 6:
            return []

        ans = [0] * n
        for idx in range(n_sum):
            ans[idx % n] += 1
        
        return ans if all(ans) else []


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.missingRolls(rolls = [3, 2, 4, 3], mean = 4, n = 2)
    assert test1 == [6, 6]

    test2 = sol.missingRolls(rolls = [1, 5, 6], mean = 3, n = 4)
    assert test2 == [3, 2, 2, 2]

    test3 = sol.missingRolls(rolls = [1, 2, 3, 4], mean = 6, n = 4)
    assert test3 == []
