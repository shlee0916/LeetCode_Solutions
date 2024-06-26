'''
https://leetcode.com/problems/count-number-of-nice-subarrays/description/?envType=daily-question&envId=2024-06-26
'''

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        cur_odd = k
        count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                cur_odd -= 1
                count = 0
            
            while cur_odd == 0:
                if nums[left] % 2 == 1:
                    cur_odd += 1
                left += 1
                count += 1

            ans += count
            
        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numberOfSubarrays(nums = [1, 1, 2, 1, 1], k = 3)
    assert test1 == 2

    test2 = sol.numberOfSubarrays(nums = [2, 4, 6], k = 1)
    assert test2 == 0

    test3 = sol.numberOfSubarrays(nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k = 2)
    assert test3 == 16
    