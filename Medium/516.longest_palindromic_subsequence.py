'''
https://leetcode.com/problems/longest-palindromic-subsequence/description/
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[0] * length for _ in range(length)]

        for pivot in range(length - 1, -1, -1):
            dp[pivot][pivot] = 1
            for ch_idx in range(pivot + 1, length):
                if s[pivot] == s[ch_idx]:
                    dp[pivot][ch_idx] = 2 + dp[pivot + 1][ch_idx - 1]
                else:
                    dp[pivot][ch_idx] = max(dp[pivot][ch_idx - 1], dp[pivot + 1][ch_idx])
            
        return dp[0][-1]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.longestPalindromeSubseq(s = "bbbab")
    assert test1 == 4

    test2 = sol.longestPalindromeSubseq(s = "cbbd")
    assert test2 == 2
