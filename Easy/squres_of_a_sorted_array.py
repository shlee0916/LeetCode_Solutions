'''
https://leetcode.com/problems/squares-of-a-sorted-array/description/
'''

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        res = []
        while left <= right:
            left_val = abs(nums[left])
            right_val = abs(nums[right])

            if left_val > right_val:
                res.append(left_val * left_val)
                left += 1
            else:
                res.append(right_val * right_val)
                right -= 1

        return res[::-1]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.sortedSquares(nums = [-4, -1, 0, 3, 10])
    assert test1 == [0, 1, 9, 16, 100]

    test2 = sol.sortedSquares(nums = [-7, -3, 2, 3, 11])
    assert test2 == [4, 9, 9, 49, 121]
    