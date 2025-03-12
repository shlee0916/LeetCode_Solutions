'''
https://leetcode.com/problems/find-the-longest-equal-subarray/
'''

from collections import defaultdict

from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        max_len = 0
        left = 0
        cnt = defaultdict(int)
        for right in range(len(nums)):
            cnt[nums[right]] += 1
            max_len = max(max_len, cnt[nums[right]])

            if right - left + 1 - max_len > k:
                cnt[nums[left]] -= 1
                left += 1

        return max_len


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.longestEqualSubarray(nums = [1, 3, 2, 3, 1, 3], k = 3)
    assert test1 == 3
    
    test2 = sol.longestEqualSubarray(nums = [1, 1, 2, 2, 1, 1], k = 2)
    assert test2 == 4
    