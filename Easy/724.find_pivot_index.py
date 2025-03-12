'''
https://leetcode.com/problems/find-pivot-index/description/
'''

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for idx, num in enumerate(nums):
            right_sum -= num

            if left_sum == right_sum:
                return idx

            left_sum += num

        return -1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.pivotIndex(nums = [1, 7, 3, 6, 5, 6])
    assert test1 == 3
    
    test2 = sol.pivotIndex(nums = [1, 2, 3])
    assert test2 == -1
    
    test3 = sol.pivotIndex(nums = [2, 1, -1])
    assert test3 == 0
    