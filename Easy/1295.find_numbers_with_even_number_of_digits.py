'''
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/?envType=daily-question&envId=2025-04-30
'''

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findNumbers(nums = [12, 345, 2, 6, 7896])
    assert test1 == 2

    test2 = sol.findNumbers(nums = [555, 901, 482, 1771])
    assert test2 == 1
