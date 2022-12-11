'''
https://leetcode.com/problems/longest-increasing-subsequence/description/
'''

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        right_nums = [0] * len(nums)
        length = 0

        for num in nums:
            left, right = 0, length

            while left != right:
                mid = (left + right) // 2

                if right_nums[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            right_nums[left] = num
            length = max(length, left + 1)

        return length


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print(test1, 4)
    assert test1 == 4
    
    test2 = sol.lengthOfLIS([0, 1, 0, 3, 2, 3])
    print(test2, 4)
    assert test2 == 4
    
    test3 = sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7])
    print(test3, 1)
    assert test3 == 1
    