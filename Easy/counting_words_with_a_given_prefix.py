'''
https://leetcode.com/problems/counting-words-with-a-given-prefix/?envType=daily-question&envId=2025-01-09
'''

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.prefixCount(words = ["pay", "attention", "practice", "attend"], pref = "at")
    assert test1 == 2

    test2 = sol.prefixCount(words = ["leetcode", "win", "loops", "success"], pref = "code")
    assert test2 == 0
    