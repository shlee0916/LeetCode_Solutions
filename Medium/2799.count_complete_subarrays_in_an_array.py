'''
https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=daily-question&envId=2025-04-24
'''

from collections import defaultdict

from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))

        left = 0
        cur_set = defaultdict(int)
        ans = 0
        for right in range(len(nums)):
            cur_set[nums[right]] += 1

            while len(cur_set) == target:
                ans += len(nums) - right
                cur_set[nums[left]] -= 1
                if cur_set[nums[left]] == 0:
                    del cur_set[nums[left]]

                left += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countCompleteSubarrays(nums = [1, 3, 1, 2, 2])
    assert test1 == 4

    test2 = sol.countCompleteSubarrays(nums = [5, 5, 5, 5])
    assert test2 == 10
