'''
https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
'''

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        begin = 0
        end = len(nums) - 1
        result = [pivot] * (end + 1)
        for idx, num in enumerate(nums):
            if num < pivot:
                result[begin], begin = num, begin + 1
            if nums[-idx - 1] > pivot:
                result[end], end = nums[-idx - 1], end - 1

        return result


# Easy straight forward solution
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        pivot_num = 0

        for num in nums:
            if num < pivot:
                result.append(num)
            if num == pivot:
                pivot_num += 1

        result.extend([pivot] * pivot_num)

        for num in nums:
            if num > pivot:
                result.append(num)

        return result


if __name__ == "__mina__":
    sol = Solution()

    test1 = sol.pivotArray(nums = [9, 12, 5, 10, 14, 3, 10], pivot = 10)
    assert test1 == [9, 5, 3, 10, 10, 12, 14]

    test2 = sol.pivotArray(nums = [-3, 4, 3, 2], pivot = 2)
    assert test2 == [-3, 2, 4, 3]
