'''
https://leetcode.com/problems/steps-to-make-array-non-decreasing/description/
'''

from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = [(nums[-1], 0)]

        res = 0
        for num in nums[::-1][1:]:
            cnt = 0

            while stack and stack[-1][0] < num:
                cnt = max(cnt + 1, stack[-1][1])
                stack.pop()

            stack.append((num, cnt))
            res = max(res, cnt)

        return res
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.totalSteps(nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11])
    assert test1 == 3

    test2 = sol.totalSteps(nums = [4, 5, 7, 7, 13])
    assert test2 == 0
