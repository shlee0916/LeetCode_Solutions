'''
https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/?envType=daily-question&envId=2023-11-07
'''

from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrive_time = [(d - 1) / s for d, s in zip(dist, speed)]

        for idx, time in enumerate(sorted(arrive_time)):
            if idx > time:
                return idx

        return len(arrive_time)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.eliminateMaximum(dist = [1, 3, 4], speed = [1, 1, 1])
    assert test1 == 3

    test2 = sol.eliminateMaximum(dist = [1, 1, 2, 3], speed = [1, 1, 1, 1])
    assert test2 == 1

    test3 = sol.eliminateMaximum(dist = [3, 2, 4], speed = [5, 3, 2])
    assert test3 == 1
    