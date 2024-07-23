'''
https://leetcode.com/problems/sort-array-by-increasing-frequency/?envType=daily-question&envId=2024-07-23
'''

from collections import Counter

from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_cnt = list(Counter(nums).items())
        nums_cnt.sort(key = lambda x: (x[1], -x[0]))

        ans = []
        for num, cnt in nums_cnt:
            ans += [num] * cnt

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.frequencySort(nums = [1, 1, 2, 2, 2, 3])
    assert test1 == [3, 1, 1, 2, 2, 2]

    test2 = sol.frequencySort(nums = [2, 3, 1, 3, 2])
    assert test2 == [1, 3, 3, 2, 2]

    test3 = sol.frequencySort(nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1])
    assert test3 == [5, -1, 4, 4, -6, -6, 1, 1, 1]
    