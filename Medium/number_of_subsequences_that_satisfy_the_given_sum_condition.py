'''
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
'''

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        mod = 10 ** 9 + 7
        res = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += pow(2, right - left, mod)
                left += 1

        return res % mod


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numSubseq(nums = [3, 5, 6, 7], target = 9)
    assert test1 == 4
    
    test2 = sol.numSubseq(nums = [3, 3, 6, 8], target = 10)
    assert test2 == 6
    
    test3 = sol.numSubseq(nums = [2, 3, 3, 4, 6, 7], target = 12)
    assert test3 == 61
    