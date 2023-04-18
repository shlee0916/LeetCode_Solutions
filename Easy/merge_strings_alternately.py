'''
https://leetcode.com/problems/merge-strings-alternately/description/
'''

from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""

        word1_len = len(word1)
        word2_len = len(word2)
        for idx in range(word1_len + word2_len):
            if idx < word1_len:
                new_str += word1[idx]
            if idx < word2_len:
                new_str += word2[idx]

        return new_str
    

    def mergeAlternately_oneline(self, word1: str, word2: str) -> str:
        return ''.join(ch1 + ch2 for ch1, ch2 in zip_longest(word1, word2, fillvalue=''))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.mergeAlternately(word1 = "abc", word2 = "pqr")
    assert test1 == "apbqcr"

    test2 = sol.mergeAlternately(word1 = "ab", word2 = "pqrs")
    assert test2 == "apbqrs"

    test3 = sol.mergeAlternately(word1 = "abcd", word2 = "pq")
    assert test3 == "apbqcd"
