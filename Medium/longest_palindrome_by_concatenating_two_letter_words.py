'''
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
'''
from typing import List
from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_map = defaultdict(int)
        
        length = 0
        same = 0
        for word in words:
            if word[0] == word[1]:
                if word_map[word] >= 1:
                    word_map[word] -= 1
                    length += 4
                    same -= 1
                else:
                    word_map[word] += 1
                    same += 1
            else:
                if word_map[word[::-1]] > 0:
                    word_map[word[::-1]] -= 1
                    length += 4
                else:
                    word_map[word] += 1
        
        if same > 0:
            length += 2
            
        return length
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.longestPalindrome(["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"])
    print(test1,26)
    assert test1 == 26
    
    test2 = sol.longestPalindrome(["lc","cl","gg"])
    print(test2,6)
    assert test2 == 6
    
    test3 = sol.longestPalindrome(["ab","ty","yt","lc","cl","ab"])
    print(test3,8)
    assert test3 == 8