'''
https://leetcode.com/problems/missing-number/description/
'''

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums) + 1)) - set(nums)).pop()


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.missingNumber([3, 0, 1])
    assert test1 == 2
    
    test2 = sol.missingNumber([0, 1])
    assert test2 == 2
    
    test3 = sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
    assert test3 == 8
    