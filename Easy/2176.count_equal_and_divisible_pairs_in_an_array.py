'''
https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/?envType=daily-question&envId=2025-04-17
'''

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx1 + 1:], idx1 + 1):
                if num1 == num2 and (idx1 * idx2) % k == 0:
                    ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countPairs(nums = [3, 1, 2, 2, 2, 1, 3], k = 2)
    assert test1 == 4

    test2 = sol.countPairs(nums = [1, 2, 3, 4], k = 1)
    assert test2 == 0
    