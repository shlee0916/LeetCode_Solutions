'''
https://leetcode.com/problems/decode-ways/
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1

        for idx in range(2, len(s) + 1):
            if 0 < int(s[idx - 1 : idx]):
                dp[idx] += dp[idx - 1]
            
            if 10 <= int(s[idx - 2 : idx]) <= 26:
                dp[idx] += dp[idx - 2]

        return dp[-1]
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numDecodings(s = "12")
    assert test1 == 2

    test2 = sol.numDecodings(s = "226")
    assert test2 == 3

    test3 = sol.numDecodings(s = "06")
    assert test3 == 0
    