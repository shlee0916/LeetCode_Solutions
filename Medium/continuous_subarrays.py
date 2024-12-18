'''
https://leetcode.com/problems/continuous-subarrays/description/?envType=daily-question&envId=2024-12-18
'''

from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = right = 0
        freq_map = {}
        ans = 0

        while right < len(nums):
            freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1

            while max(freq_map) - min(freq_map) > 2:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                
                left += 1

            ans += right - left + 1
            right += 1
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.continuousSubarrays(nums = [5, 4, 2, 4])
    assert test1 == 8

    test2 = sol.continuousSubarrays(nums = [1, 2, 3])
    assert test2 == 6
    