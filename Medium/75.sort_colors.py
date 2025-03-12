'''
https://leetcode.com/problems/sort-colors/description/
'''

from collections import Counter

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = Counter(nums)
        new_num = [0] * counter[0] + [1] * counter[1] + [2] * counter[2]
        nums[:] = new_num[:]


if __name__ == "__main__":
    sol = Solution()

    test1_list = [2, 0, 2, 1, 1, 0]
    test1 = sol.sortColors(nums = test1_list)
    print(test1_list, [0, 0, 1, 1, 2, 2])
    assert test1_list == [0, 0, 1, 1, 2, 2]

    test2_list = [2, 0, 1]
    test2 = sol.sortColors(nums = test2_list)
    print(test2_list, [0, 1, 2])
    assert test2_list == [0, 1, 2]
