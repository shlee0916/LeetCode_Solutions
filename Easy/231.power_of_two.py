'''
https://leetcode.com/problems/power-of-two/
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return pow(2, n, n) == 0 if n > 0 else False


if __name__ == "__main__":
    sol = Solution()

    print(sol.isPowerOfTwo(39), False)
    print(sol.isPowerOfTwo(4), True)