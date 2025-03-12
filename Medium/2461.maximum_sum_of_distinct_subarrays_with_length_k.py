'''
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/?envType=daily-question&envId=2024-11-19
'''

from collections import Counter

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cur_sum = sum(nums[:k])
        cur_sub = Counter(nums[:k])

        if len(cur_sub) == k:
            ans = cur_sum

        for idx in range(k, len(nums)):
            cur_sum += nums[idx] - nums[idx - k]
            cur_sub[nums[idx]] += 1
            cur_sub[nums[idx - k]] -= 1

            if cur_sub[nums[idx - k]] == 0:
                cur_sub.pop(nums[idx - k])
            
            if len(cur_sub) == k:
                ans = max(ans, cur_sum)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumSubarraySum(nums = [1, 5, 4, 2, 9, 9, 9], k = 3)
    assert test1 == 15

    test2 = sol.maximumSubarraySum(nums = [4, 4, 4], k = 3)
    assert test2 == 0
    