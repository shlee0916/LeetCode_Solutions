'''
https://leetcode.com/problems/power-of-four/description/
'''

from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isPowerOfFour(16)
    assert test1 == True
    
    test2 = sol.isPowerOfFour(5)
    assert test2 == False
    
    test3 = sol.isPowerOfFour(1)
    assert test3 == True
    