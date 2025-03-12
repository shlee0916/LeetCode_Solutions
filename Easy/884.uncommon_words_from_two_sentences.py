'''
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
'''

from collections import Counter

from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = Counter((s1 + " " + s2).split())

        return [word for word, num in words.items() if num == 1]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour")
    assert test1 == ["sweet", "sour"]

    test2 = sol.uncommonFromSentences(s1 = "apple apple", s2 = "banana")
    assert test2 == ["banana"]
    