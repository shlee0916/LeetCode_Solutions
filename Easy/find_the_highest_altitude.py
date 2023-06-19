'''
https://leetcode.com/problems/find-the-highest-altitude/description/
'''

from itertools import accumulate
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max([0] + list(accumulate(gain)))
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.largestAltitude(gain = [-5, 1, 5, 0, -7])
    assert test1 == 1

    test2 = sol.largestAltitude(gain = [-4, -3, -2, -1, 4, 3, 2])
    assert test2 == 0
    