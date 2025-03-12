'''
https://leetcode.com/problems/find-words-containing-character/
'''

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []

        for idx, word in enumerate(words):
            if x in word:
                ans.append(idx)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findWordsContaining(words = ["leet", "code"], x = "e")
    assert test1 == [0, 1]
    
    test2 = sol.findWordsContaining(words = ["abc", "bcd", "aaaa", "cbc"], x = "a")
    assert test2 == [0, 2]
    
    test3 = sol.findWordsContaining(words = ["abc", "bcd", "aaaa", "cbc"], x = "z")
    assert test3 == []
    