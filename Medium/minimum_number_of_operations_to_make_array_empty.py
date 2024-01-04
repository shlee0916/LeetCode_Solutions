'''
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/?envType=daily-question&envId=2024-01-04
'''

from collections import Counter

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_cnt = Counter(nums)

        if min(nums_cnt.values()) == 1:
            return -1

        return sum(cnt // 3 + (cnt % 3 > 0) for cnt in nums_cnt.values())


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minOperations(nums = [2, 3, 3, 2, 2, 4, 2, 3, 4])
    assert test1 == 4

    test2 = sol.minOperations(nums = [2, 1, 2, 2, 3, 3])
    assert test2 == -1
    