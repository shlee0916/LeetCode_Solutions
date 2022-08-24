'''
https://leetcode.com/problems/power-of-three/
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and pow(3, n, n) == 0


if __name__ == "__main__":
    sol = Solution()

    print(sol.isPowerOfThree(7), False)
    print(sol.isPowerOfThree(9), True)