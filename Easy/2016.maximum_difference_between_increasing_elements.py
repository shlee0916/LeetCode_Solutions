'''
https://leetcode.com/problems/maximum-difference-between-increasing-elements/?envType=daily-question&envId=2025-06-16
'''

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        minn = float("inf")

        for idx, num in enumerate(nums):
            if idx > 0 and num > minn:
                ans = max(ans, num - minn)

            minn = min(minn, num)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumDifference(nums = [7, 1, 5, 4])
    assert test1 == 4

    test2 = sol.maximumDifference(nums = [9, 4, 3, 2])
    assert test2 == -1

    test3 = sol.maximumDifference(nums = [1, 5, 2, 10])
    assert test3 == 9
    