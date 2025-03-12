'''
https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2023-12-06
'''

class Solution:
    def totalMoney(self, n: int) -> int:
        num_weeks = n // 7

        total = num_weeks * 28
        total += num_weeks * (num_weeks - 1) * 7 // 2

        left_days = n % 7
        extra = num_weeks + 1

        return total + (left_days * (left_days - 1) // 2) + extra * left_days


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.totalMoney(n = 4)
    assert test1 == 10

    test2 = sol.totalMoney(n = 10)
    assert test2 == 37

    test3 = sol.totalMoney(20)
    assert test3 == 96
    