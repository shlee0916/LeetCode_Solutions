'''
https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/?envType=daily-question&envId=2025-05-27
'''

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        m_div_total = m * (n // m) * (n // m + 1)

        return total - m_div_total


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.differenceOfSums(n = 10, m =3)
    assert test1 == 19

    test2 = sol.differenceOfSums(n = 5, m = 6)
    assert test2 == 15

    test3 = sol.differenceOfSums(n = 5, m = 1)
    assert test3 == -15
