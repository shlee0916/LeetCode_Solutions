'''
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/
'''

from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.canBeEqual(target = [1, 2, 3, 4], arr = [2, 4, 1, 3])
    assert test1 == True
    
    test2 = sol.canBeEqual(target = [7], arr = [7])
    assert test2 == True
    
    test3 = sol.canBeEqual(target = [3, 7, 9], arr = [3, 7, 11])
    assert test3 == False
    