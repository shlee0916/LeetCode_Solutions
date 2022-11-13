'''
https://leetcode.com/problems/reverse-words-in-a-string/description/
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join([word.strip() for word in words[::-1]])
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.reverseWords("the sky is blue")
    print(test1, "blue is sky the")
    assert test1 == "blue is sky the"
    
    test2 = sol.reverseWords("  hello world  ")
    print(test2, "world hello")
    assert test2 == "world hello"
    
    test3 = sol.reverseWords("a good   example")
    print(test3, "example good a")
    assert test3 == "example good a"
    