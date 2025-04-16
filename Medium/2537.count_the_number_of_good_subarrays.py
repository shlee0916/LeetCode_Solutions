'''
https://leetcode.com/problems/count-the-number-of-good-subarrays/?envType=daily-question&envId=2025-04-16
'''

from collections import defaultdict

from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        cur_pair = 0
        nums_cnt = defaultdict(int)

        for right in range(len(nums)):
            nums_cnt[nums[right]] += 1

            cur_pair += (nums_cnt[nums[right]] - 1)

            while cur_pair >= k and left < right:
                cur_pair -= (nums_cnt[nums[left]] - 1)
                nums_cnt[nums[left]] -= 1

                left += 1
            
            ans += left

        return ans
