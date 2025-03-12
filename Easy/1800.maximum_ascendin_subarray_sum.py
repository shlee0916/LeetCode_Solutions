'''
https://leetcode.com/problems/maximum-ascending-subarray-sum/?envType=daily-question&envId=2025-02-04
'''

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum = nums.pop(0)
        ans = cur_sum
        prev = cur_sum

        for num in nums:
            if num > prev:
                cur_sum += num
                ans = max(ans, cur_sum)
            else:
                cur_sum = num
            prev = num

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxAscendingSum(nums = [10, 20, 30, 5, 10, 50])
    assert test1 == 65

    test2 = sol.maxAscendingSum(nums = [10, 20, 30, 40, 50])
    assert test2 == 150

    test3 = sol.maxAscendingSum(nums = [12, 17, 15, 13, 10, 11, 12])
    assert test3 == 33
    