'''
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/
'''

from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        res = []

        for idx, num in enumerate(nums):
            new_num = (right_sum - (len(nums) - idx) * num) + (idx * num - left_sum)

            res.append(new_num)

            left_sum += num
            right_sum -= num

        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getSumAbsoluteDifferences(nums = [2, 3, 5])
    assert test1 == [4, 3, 5]

    test2 = sol.getSumAbsoluteDifferences(nums = [1, 4, 6, 8, 10])
    assert test2 == [24, 15, 13, 15, 21]
    