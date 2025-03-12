'''
https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = abs(n)

        ans = 1
        while n:
            if n % 2:
                ans *= x
            x *= x
            n //= 2

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.myPow(x = 2.00000, n = 10)
    assert test1 == 1024.00000
    
    test2 = sol.myPow(x = 2.10000, n = 3)
    assert round(test2, 6) == 9.26100
    
    test3 = sol.myPow(x = 2.00000, n = -2)
    assert test3 == 0.25000
    