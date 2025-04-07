'''
https://leetcode.com/problems/partition-equal-subset-sum/description/?envType=daily-question&envId=2025-04-07
'''

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        dp = [False] * (total + 1)
        dp[0] = True
        target = total // 2
        for num in nums:
            for sub_sum in range(target, num - 1, -1):
                dp[sub_sum] = dp[sub_sum] or dp[sub_sum - num]

        return dp[target]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.canPartition(nums = [1, 5, 11, 5])
    assert test1 == True

    test2 = sol.canPartition(nums = [1, 2, 3, 5])
    assert test2 == False
    