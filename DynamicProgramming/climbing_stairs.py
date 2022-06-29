'''
https://leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        cur = 0
        ppre, pre = 1, 2
        for _ in range(3, n + 1):
            cur = pre + ppre
            ppre = pre
            pre = cur
                    
        return cur
    

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.climbStairs(3))
    print(sol.climbStairs(5))