'''
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
'''

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.mostWordsFound(sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
    assert test1 == 6
    
    test2 = sol.mostWordsFound(sentences = ["please wait", "continue to fight", "continue to win"])
    assert test2 == 3
    