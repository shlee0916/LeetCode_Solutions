'''
https://leetcode.com/problems/find-if-array-can-be-sorted/?envType=daily-question&envId=2024-11-06
'''

from itertools import groupby

from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        groups = groupby(nums, key = lambda x: x.bit_count()) # python >= 3.10

        new_nums = []
        for _, grp in groups:
            new_nums.extend(sorted(grp))

        return new_nums == sorted(nums)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.canSortArray(nums = [8, 4, 2, 30, 15])
    assert test1 == True
    
    test2 = sol.canSortArray(nums = [1, 2, 3, 4, 5])
    assert test2 == True

    test3 = sol.canSortArray(nums = [3, 16, 8, 4, 2])
    assert test3 == False
