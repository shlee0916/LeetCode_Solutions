'''
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/?envType=daily-question&envId=2023-12-01
'''

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"])
    assert test1 == True

    test2 = sol.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"])
    assert test2 == False

    test3 = sol.arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"])
    assert test3 == True
    