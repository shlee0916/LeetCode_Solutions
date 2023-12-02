'''
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/?envType=daily-question&envId=2023-12-02
'''

from collections import Counter

from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        chars_cnt = Counter(chars)
        for word in words:
            word_cnt = Counter(word)
            if all(word_cnt[ch] <= chars_cnt[ch] for ch in word):
                ans += len(word)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countCharacters(words = ["cat", "bt", "hat", "tree"], chars = "atach")
    assert test1 == 6
    
    test2 = sol.countCharacters(words = ["hello", "world", "leetcode"], chars = "welldonehoneyr")
    assert test2 == 10
    