'''
https://leetcode.com/problems/concatenation-of-array/description/
'''

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.getConcatenation(nums = [1, 2, 1])
    assert test1 == [1, 2, 1, 1, 2, 1]
    
    test2 = sol.getConcatenation(nums = [1, 3, 2, 1])
    assert test2 == [1, 3, 2, 1, 1, 3, 2, 1]
    