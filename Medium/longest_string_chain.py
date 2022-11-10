'''
https://leetcode.com/problems/longest-string-chain/description/
'''
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cache = {}

        for word in sorted(words, key = len):
            cache[word] = max(cache.get(word[:idx] + word[idx + 1:], 0) + 1 for idx in range(len(word)))

        return max(cache.values())


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"])
    print(test1, 4)
    assert test1 == 4

    test2 = sol.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"])
    print(test2, 5)
    assert test2 == 5

    test3 = sol.longestStrChain(["abcd", "dbqca"])
    print(test3, 1)
    assert test3 == 1
