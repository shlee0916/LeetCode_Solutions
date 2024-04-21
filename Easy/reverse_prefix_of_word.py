'''
https://leetcode.com/problems/reverse-prefix-of-word/
'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)

        if idx:
            return word[:idx + 1][::-1] + word[idx + 1:]

        return word
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.reversePrefix(word = "abcdefd", ch = "d")
    assert test1 == "dcbaefd"
    
    test2 = sol.reversePrefix(word = "xyxzxe", ch = "z")
    assert test2 == "zxyxxe"
    
    test3 = sol.reversePrefix(word = "abcd", ch = "z")
    assert test3 == "abcd"
    