'''
https://leetcode.com/problems/repeated-substring-pattern/description/
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_fold = "".join( (s[1:], s[:-1]) )
        
        return s in s_fold
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.repeatedSubstringPattern(s = "abab")
    assert test1 == True
    
    test2 = sol.repeatedSubstringPattern(s = "aba")
    assert test2 == False
    
    test3 = sol.repeatedSubstringPattern(s = "abcabcabcabc")
    assert test3 == True
    