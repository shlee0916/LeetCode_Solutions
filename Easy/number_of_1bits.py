'''
https://leetcode.com/problems/number-of-1-bits/
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
            
        return cnt


if __name__ == "__main__":
    sol = Solution()

    print(sol.hammingWeight(11), 3)