'''
https://leetcode.com/problems/find-and-replace-pattern/description/
'''

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def get_word_map(w):
            word_map = {}
            
            return [word_map.setdefault(ch, len(word_map)) for ch in w]

        return [word for word in words if get_word_map(word) == get_word_map(pattern)]
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findAndReplacePattern(words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern = "abb")
    assert test1 == ["mee", "aqq"]
    
    test2 = sol.findAndReplacePattern(words = ["a", "b", "c"], pattern = "a")
    assert test2 == ["a","b","c"]
    