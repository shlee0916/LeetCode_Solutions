'''
https://leetcode.com/problems/neighboring-bitwise-xor/?envType=daily-question&envId=2025-01-17
'''

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for der in derived:
            ans ^= der

        return ans == 0


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.doesValidArrayExist(derived = [1, 1, 0])
    assert test1 == True

    test2 = sol.doesValidArrayExist(derived = [1, 1])
    assert test2 == True

    test3 = sol.doesValidArrayExist(derived = [1, 0])
    assert test3 == False
    