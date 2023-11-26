'''
https://leetcode.com/problems/sum-of-unique-elements/description/
'''

from collections import Counter

from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num, val in Counter(nums).items() if val == 1)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.sumOfUnique(nums = [1, 2, 3, 2])
    assert test1 == 4
    
    test2 = sol.sumOfUnique(nums = [1, 1, 1, 1, 1])
    assert test2 == 0
    
    test3 = sol.sumOfUnique(nums = [1, 2, 3, 4, 5])
    assert test3 == 15
    