'''
https://leetcode.com/problems/contains-duplicate/
'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums) == len(set(nums)) else True


if __name__ == "__main__":
    sol = Solution()

    print(sol.containsDuplicate([1, 2, 3, 1]))