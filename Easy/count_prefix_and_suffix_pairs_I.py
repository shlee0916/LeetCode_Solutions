'''
https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/?envType=daily-question&envId=2025-01-08
'''

from typing import List


class Solution:
    def _is_prefix_and_suffix(self, str1: str, str2: str) -> bool:
        if str2.startswith(str1) and str2.endswith(str1):
            return True
        else:
            return False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for first in range(len(words) - 1):
            for second in range(first + 1, len(words)):
                ans += self._is_prefix_and_suffix(words[first], words[second]) == True

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countPrefixSuffixPairs(words = ["a", "aba", "ababa", "aa"])
    assert test1 == 4

    test2 = sol.countPrefixSuffixPairs(words = ["pa", "papa", "ma", "mama"])
    assert test2 == 2

    test3 = sol.countPrefixSuffixPairs(words = ["abab", "ab"])
    assert test3 == 0
    