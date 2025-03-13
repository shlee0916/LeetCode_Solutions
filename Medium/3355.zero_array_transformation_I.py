'''
https://leetcode.com/problems/zero-array-transformation-i/
'''

from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)

        for left, right in queries:
            diff[left] += 1
            diff[right + 1] -= 1

        cur_val = 0
        for idx in range(len(nums)):
            cur_val += diff[idx]

            if cur_val < nums[idx]:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.isZeroArray(nums = [1, 0, 1], queries = [[0, 2]])
    assert test1 == True

    test2 = sol.isZeroArray(nums = [4, 3, 2, 1], queries = [[1, 3], [0, 2]])
    assert test2 == False
    