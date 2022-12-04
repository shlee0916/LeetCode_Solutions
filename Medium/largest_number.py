'''
https://leetcode.com/problems/largest-number/description/
'''

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = map(str, nums)
        comp = lambda x, y: -1 if x + y > y + x else 1 if x + y < y + x else 0
        return str(int("".join(sorted(nums, key = cmp_to_key(comp)))))
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.largestNumber([10,2])
    print(test1,"210")
    assert test1 == "210"
    
    test2 = sol.largestNumber([3,30,34,5,9])
    print(test2,"9534330")
    assert test2 == "9534330"