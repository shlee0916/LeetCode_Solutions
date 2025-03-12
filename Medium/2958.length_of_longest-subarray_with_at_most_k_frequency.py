'''
https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/?envType=daily-question&envId=2024-03-28
'''

from collections import defaultdict

from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        left = 0

        for right in range(len(nums)):
            cnt[nums[right]] += 1

            while cnt[nums[right]] > k:
                cnt[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

         
if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxSubarrayLength(nums = [1, 2, 3, 1, 2, 3, 1, 2], k = 2)
    assert test1 == 6

    test2 = sol.maxSubarrayLength(nums = [1, 2, 1, 2, 1, 2, 1, 2], k = 1)
    assert test2 == 2

    test3 = sol.maxSubarrayLength(nums = [5, 5, 5, 5, 5, 5, 5], k = 4)
    assert test3 == 4
    