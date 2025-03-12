'''
https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
'''

from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()

        remove_idx = len(arr) // 20
        length = len(arr)

        return sum(arr[remove_idx : length - remove_idx]) / (length - (2 * remove_idx))


if __name__ == "__main__":
    def _round(num: float):
        return round(num, 5)

    sol = Solution()

    test1 = sol.trimMean(arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3])
    assert _round(test1) == 2.00000

    test2 = sol.trimMean(arr = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0])
    assert _round(test2) == 4.00000

    test3 = sol.trimMean(arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4])
    assert _round(test3) == 4.77778
