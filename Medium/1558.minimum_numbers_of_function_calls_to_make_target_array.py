'''
https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/description/
'''

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minus = 0
        divide = 0
        for num in nums:
            cur_divide = 0
            while num:
                if num % 2 == 1:
                    minus += 1
                    num -= 1
                else:
                    num //= 2
                    cur_divide += 1

            divide = max(cur_divide, divide)

        return minus + divide


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minOperations(nums = [1, 5])
    assert test1 == 5

    test2 = sol.minOperations(nums = [2, 2])
    assert test2 == 3

    test3 = sol.minOperations(nums = [4, 2, 5])
    assert test3 == 6
    