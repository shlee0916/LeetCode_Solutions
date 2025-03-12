'''
https://leetcode.com/problems/word-break/
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] = dp[i-len(word)] | dp[i]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak("leetcode", ["leet","code"]), True)
    print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]), False)
    print(sol.wordBreak("applepenapple", ["apple","pen"]), True)