'''
https://leetcode.com/problems/2-keys-keyboard/description/?envType=daily-question&envId=2024-08-19
'''

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        step = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                step += factor
                n //= factor

            factor += 1

        return step


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minSteps(n = 3)
    assert test1 == 3

    test2 = sol.minSteps(n = 1)
    assert test2 == 0
    