'''
https://leetcode.com/problems/first-missing-positive/?envType=daily-question&envId=2024-03-26
'''

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        length = len(nums)

        for idx in range(length):
            if nums[idx] < 0 or nums[idx] >= length:
                nums[idx] = 0

        for idx in range(length):
            nums[nums[idx] % length] += length

        for idx in range(1, length):
            if nums[idx] // length == 0:
                return idx
        
        return length
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.firstMissingPositive(nums = [1, 2, 0])
    assert test1 == 3

    test2 = sol.firstMissingPositive(nums = [3, 4, -1, 1])
    assert test2 == 2

    test3 = sol.firstMissingPositive(nums = [7, 8, 9, 11, 12])
    assert test3 == 1
