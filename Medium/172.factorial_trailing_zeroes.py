'''
https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0

        while n > 0:
            ans += n // 5

            n //= 5

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.trailingZeroes(n = 3)
    assert test1 == 0

    test2 = sol.trailingZeroes(n = 5)
    assert test2 == 1

    test3 = sol.trailingZeroes(n = 0)
    assert test3 == 0
    