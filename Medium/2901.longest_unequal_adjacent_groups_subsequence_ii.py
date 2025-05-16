'''
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/?envType=daily-question&envId=2025-05-16
'''

from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def diff(word1, word2):
            if len(word1) != len(word2):
                return False
                
            return sum(ch1 != ch2 for ch1, ch2 in zip(word1, word2)) == 1

        length = len(groups)
        dp = [1] * length
        prev = [-1] * length
        res = 0

        for idx in range(length):
            for prev_idx in range(idx):
                if groups[idx] != groups[prev_idx] and \
                   diff(words[idx], words[prev_idx]) and \
                   dp[idx] < dp[prev_idx] + 1:
                   dp[idx] = dp[prev_idx] + 1
                   prev[idx] = prev_idx

            res = max(dp[idx], res)

        ans = []
        ans_idx = dp.index(res)
        while ans_idx != -1:
            ans.append(words[ans_idx])
            ans_idx = prev[ans_idx]
        
        return ans[::-1]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getWordsInLongestSubsequence(words = ["bab", "dab", "cab"], groups = [1, 2, 2])
    assert test1 == ["bab", "dab"]

    test2 = sol.getWordsInLongestSubsequence(words = ["a", "b", "c", "d"], groups = [1, 2, 3, 4])
    assert test2 == ["a", "b", "c", "d"]
