'''
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/?envType=daily-question&envId=2024-03-29
'''

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        cur_cnt = 0
        left = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == max_num:
                cur_cnt += 1

            while cur_cnt >= k:
                if nums[left] == max_num:
                    cur_cnt -= 1
                left += 1

            ans += left

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countSubarrays(nums = [1, 3, 2, 3, 3], k = 2)
    assert test1 == 6

    test2 = sol.countSubarrays(nums = [1, 4, 2, 1], k = 3)
    assert test2 == 0
    