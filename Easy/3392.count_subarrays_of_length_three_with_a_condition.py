'''
https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/?envType=daily-question&envId=2025-04-27
'''

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0

        for idx in range(0, len(nums) - 2):
            if nums[idx] + nums[idx + 2] == nums[idx + 1] / 2:
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countSubarrays(nums = [1, 2, 1, 4, 1])
    assert test1 == 1
    
    test2 = sol.countSubarrays(nums = [1, 1, 1])
    assert test2 == 0
    