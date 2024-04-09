'''
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
'''

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        idx = 0
        while idx < len(nums) and idx < k and nums[idx] < 0:
            nums[idx] = -nums[idx]
            idx += 1

        return sum(nums) - (k - idx) % 2 * min(nums) * 2


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.largestSumAfterKNegations(nums = [4, 2, 3], k = 1)
    assert test1 == 5
    
    test2 = sol.largestSumAfterKNegations(nums = [3, -1, 0, 2], k = 3)
    assert test2 == 6
    
    test3 = sol.largestSumAfterKNegations(nums = [2, -3, -1, 5, -4], k = 2)
    assert test3 == 13
    