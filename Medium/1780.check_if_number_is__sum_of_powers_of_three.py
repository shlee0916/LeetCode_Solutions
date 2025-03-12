'''
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/?envType=daily-question&envId=2025-03-04
'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1 and n % 3 != 2:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
        
        return n == 1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.checkPowersOfThree(n = 12)
    assert test1 == True
    
    test2 = sol.checkPowersOfThree(n = 91)
    assert test2 == True
    
    test3 = sol.checkPowersOfThree(n = 21)
    assert test3 == False
    