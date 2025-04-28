'''
https://leetcode.com/problems/count-subarrays-with-score-less-than-k/?envType=daily-question&envId=2025-04-28
'''

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum * (right - left + 1) >= k:
                cur_sum -= nums[left]
                left += 1

            ans += right - left + 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countSubarrays(nums = [2, 1, 4, 3, 5], k = 10)
    assert test1 == 6

    test2 = sol.countSubarrays(nums = [1, 1, 1], k = 5)
    assert test2 == 5
    