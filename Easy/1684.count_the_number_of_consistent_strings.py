'''
https://leetcode.com/problems/count-the-number-of-consistent-strings/?envType=daily-question&envId=2024-09-12
'''

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        ans = 0
        for word in words:
            if all(ch in allowed_set for ch in word):
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countConsistentStrings(allowed = "ab", words = ["ad", "bd", "aaab", "baa", "badab"])
    assert test1 == 2

    test2 = sol.countConsistentStrings(allowed = "abc", words = ["a", "b", "c", "ab", "ac", "bc", "abc"])
    assert test2 == 7

    test3 = sol.countConsistentStrings(allowed = "cad", words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"])
    assert test3 == 4
    