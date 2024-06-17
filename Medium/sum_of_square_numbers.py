'''
https://leetcode.com/problems/sum-of-square-numbers/?envType=daily-question&envId=2024-06-17
'''

from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))

        while left <= right:
            cur = left ** 2 + right ** 2

            if cur == c:
                return True

            elif cur < c:
                left += 1
            else:
                right -= 1
        
        return False


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.judgeSquareSum(c = 5)
    assert test1 == True

    test2 = sol.judgeSquareSum(c = 3)
    assert test2 == False
    