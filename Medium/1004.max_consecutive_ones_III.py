'''
https://leetcode.com/problems/max-consecutive-ones-iii/description/
'''

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start_idx = 0
        for end_idx, value in enumerate(nums):
            if value == 0:
                k -= 1
            
            if k < 0:
                if nums[start_idx] == 0:
                    k += 1
                start_idx += 1

        return end_idx - start_idx + 1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.longestOnes(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2)
    assert test1 == 6

    test2 = sol.longestOnes(nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3)
    assert test2 == 10
    