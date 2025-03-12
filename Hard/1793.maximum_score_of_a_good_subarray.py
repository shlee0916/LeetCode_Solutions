'''
https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/?envType=daily-question&envId=2023-10-22
'''

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = k
        right = k
        left_limit = 0
        right_limit = len(nums) - 1

        min_val = nums[k]
        res = nums[k]

        while left > 0 or right < right_limit:
            if left == left_limit:
                right += 1
            elif right == right_limit:
                left -= 1
            elif nums[left - 1] < nums[right + 1]:
                right += 1
            else:
                left -= 1

            min_val = min(min_val, nums[left], nums[right])
            res = max(res, min_val * (right - left + 1))

        return res
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maximumScore(nums = [1, 4, 3, 7, 4, 5], k = 3)
    assert test1 == 15
    
    test2 = sol.maximumScore(nums = [5, 5, 4, 5, 4, 1, 1, 1], k = 0)
    assert test2 == 20
    