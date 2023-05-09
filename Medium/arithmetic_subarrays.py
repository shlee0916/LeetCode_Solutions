'''
https://leetcode.com/problems/arithmetic-subarrays/description/
'''

from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []

        for start_idx, end_idx in zip(l, r):
            target = nums[start_idx : end_idx + 1]
            
            max_target = max(target)
            min_target = min(target)
            total_diff = max_target - min_target
            step = total_diff // (len(target) - 1)
            
            if step == 0:
                check = max_target == min_target
                result.append(check)
            else:
                check = set(target) == set(range(min_target, max_target + step, step))
                result.append(check)
            
        return result
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.checkArithmeticSubarrays(nums = [4, 6, 5, 9, 3, 7], l = [0, 0, 2], r = [2, 3, 5])
    assert test1 == [True, False, True]

    test2 = sol.checkArithmeticSubarrays(nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], l = [0, 1, 6, 4, 8, 7], r = [4, 4, 9, 7, 9, 10])
    assert test2 == [False, True, False, False, True, True]
