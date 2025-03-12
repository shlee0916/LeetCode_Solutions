'''
https://leetcode.com/problems/height-checker/?envType=daily-question&envId=2024-06-10
'''

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(ori != sort for ori, sort in zip(heights, sorted(heights)))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.heightChecker(heights = [1, 1, 4, 2, 1, 3])
    assert test1 == 3

    test2 = sol.heightChecker(heights = [5, 1, 2, 3, 4])
    assert test2 == 5

    test3 = sol.heightChecker(heights = [1, 2, 3, 4, 5])
    assert test3 == 0
    