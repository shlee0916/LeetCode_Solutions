'''
https://leetcode.com/problems/find-the-value-of-the-partition/
'''

from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()

        ans = float("inf")
        for idx in range(len(nums) - 1):
            ans = min(ans, nums[idx + 1] - nums[idx])

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findValueOfPartition(nums = [1, 3, 2, 4])
    assert test1 == 1

    test2 = sol.findValueOfPartition(nums = [100, 1, 10])
    assert test2 == 9
    