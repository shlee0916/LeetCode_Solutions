'''
https://leetcode.com/problems/minimum-size-subarray-sum/description/
'''

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = left = 0
        result = len(nums) + 1

        for right, num in enumerate(nums):
            total += num

            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1

        return result if result <= len(nums) else 0


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minSubArrayLen(target = 7, nums = [2, 3, 1, 2, 4, 3])
    assert test1 == 2
    
    test2 = sol.minSubArrayLen(target = 4, nums = [1, 4, 4])
    assert test2 == 1
    
    test3 = sol.minSubArrayLen(target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1])
    assert test3 == 0
    