'''
https://leetcode.com/problems/n-th-tribonacci-number/
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        tribo = [0, 1, 1]
        if n < 3:
            return tribo[n]
        else:
            while len(tribo) < n + 1:
                tribo.append(tribo[-3] + tribo[-2] + tribo[-1])
        
        return tribo[n]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.tribonacci(6))