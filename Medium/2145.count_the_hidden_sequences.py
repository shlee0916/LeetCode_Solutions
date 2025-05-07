'''
https://leetcode.com/problems/count-the-hidden-sequences/?envType=daily-question&envId=2025-04-21
'''

from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        ans = 0

        temp = [0]
        for diff in differences:
            temp.append(temp[-1] + diff)

        diff_range = max(temp) - min(temp)
        ans = upper - lower - diff_range + 1

        return ans if ans > 0 else 0


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numberOfArrays(differences = [1, -3, 4], lower = 1, upper = 6)
    assert test1 == 2

    test2 = sol.numberOfArrays(differences = [3, -4, 5, 1, -2], lower = -4, upper = 5)
    assert test2 == 4

    test3 = sol.numberOfArrays(differences = [4, -7, 2], lower = 3, upper = 6)
    assert test3 == 0
