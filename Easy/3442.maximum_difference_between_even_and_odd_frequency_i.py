'''
https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-10
'''

from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        ch_freq = Counter(s)

        max_freq = 0
        min_freq = len(s)

        for val in ch_freq.values():
            if val % 2 == 1:
                max_freq = max(max_freq, val)

            if val % 2 == 0:
                min_freq = min(min_freq, val)
            
        return max_freq - min_freq


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxDifference(s = "aaaaabbc")
    assert test1 == 3

    test2 = sol.maxDifference(s = "abcabcab")
    assert test2 == 1
    