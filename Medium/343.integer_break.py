'''
https://leetcode.com/problems/integer-break/description/?envType=daily-question&envId=2023-10-12
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        ans = [0, 0, 1, 2, 4, 6, 9]

        if n < 7:
            return ans[n]

        for idx in range(7, n + 1):
            ans.append(ans[idx - 3] * 3)

        return ans[n]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.integerBreak(n = 2)
    assert test1 == 1

    test2 = sol.integerBreak(n = 10)
    assert test2 == 36
    