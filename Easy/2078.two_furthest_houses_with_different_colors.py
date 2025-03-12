'''
https://leetcode.com/problems/two-furthest-houses-with-different-colors/
'''

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for idx, color in enumerate(colors):
            if colors[0] != color:
                ans = max(ans, idx)

        for idx, color in enumerate(colors):
            if colors[-1] != color:
                ans = max(ans, len(colors) - idx - 1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxDistance(colors = [1, 1, 1, 6, 1, 1, 1])
    assert test1 == 3

    test2 = sol.maxDistance(colors = [1, 8, 3, 8, 3])
    assert test2 == 4

    test3 = sol.maxDistance(colors = [0, 1])
    assert test3 == 1
