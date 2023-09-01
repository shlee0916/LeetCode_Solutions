'''
https://leetcode.com/problems/maximum-average-subarray-i/description/
'''

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_val = tmp_sum = sum(nums[:k])

        for idx in range(1, len(nums) - k + 1):
            tmp_sum -= nums[idx - 1]
            tmp_sum += nums[idx + k - 1]

            max_val = max(max_val, tmp_sum)

        return float(max_val) / k


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findMaxAverage(nums = [1, 12, -5, -6, 50, 3], k = 4)
    assert test1 == 12.75
    
    test2 = sol.findMaxAverage(nums = [5], k = 1)
    assert test2 == 5.0
    