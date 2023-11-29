'''
https://leetcode.com/problems/three-divisors/description/
'''

class Solution:
    def isThree(self, n: int) -> bool:
        return sum(n % num == 0 for num in range(1, n + 1)) == 3


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isThree(n = 2)
    assert test1 == False
    
    test2 = sol.isThree(n = 4)
    assert test2 == True
    