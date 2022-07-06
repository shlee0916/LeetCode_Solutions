'''
https://leetcode.com/problems/fibonacci-number/
'''

class Solution:
    def fib(self, n: int) -> int:
        fibo = [0, 1]
        if n < 2:
            return fibo[n]
        else:
            while len(fibo) < n + 1:
                fibo.append(fibo[-2] + fibo[-1])
            return fibo[-1]
        
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(6))