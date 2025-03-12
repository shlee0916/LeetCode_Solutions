'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
'''

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums) + 1)) - set(nums)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(test1, [5, 6])
    assert test1 == set([5, 6])
    
    test2 = sol.findDisappearedNumbers([1, 1])
    print(test2, [2])
    assert test2 == set([2])
    