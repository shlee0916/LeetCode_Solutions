'''
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
'''

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        for word in sorted(dictionary, key = lambda x: (-len(x), x)):
            idx = 0
            for ch in s:
                if idx < len(word) and word[idx] == ch:
                    idx += 1
            
            if idx == len(word):
                return word

        return ""


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findLongestWord(s = "abpcplea", dictionary = ["ale", "apple", "monkey", "plea"])
    assert test1 == "apple"
    
    test2 = sol.findLongestWord(s = "abpcplea", dictionary = ["a", "b", "c"])
    assert test2 == "a"
    