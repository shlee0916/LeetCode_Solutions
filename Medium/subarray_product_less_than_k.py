'''
https://leetcode.com/problems/subarray-product-less-than-k/?envType=daily-question&envId=2024-03-27
'''

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0
        left = 0
        
        cur_prod = 1
        for right in range(len(nums)):
            cur_prod *= nums[right]

            while cur_prod >= k and left <= right:
                cur_prod /= nums[left]
                left += 1
            
            cnt += right - left + 1

        return cnt
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numSubarrayProductLessThanK(nums = [10, 5, 2, 6], k = 100)
    assert test1 == 8

    test2 = sol.numSubarrayProductLessThanK(nums = [1, 2, 3], k = 0)
    assert test2 == 0
