'''
https://leetcode.com/problems/reverse-only-letters/description/
'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        begin = 0
        end = len(s) - 1
        new_str = [ch for ch in s]
        while begin < end:
            if new_str[begin].isalpha() and new_str[end].isalpha():
                new_str[begin], new_str[end] = new_str[end], new_str[begin]
                begin += 1
                end -= 1
            elif new_str[begin].isalpha() and not new_str[end].isalpha():
                end -= 1
            elif new_str[end].isalpha() and not new_str[begin].isalpha():
                begin += 1
            else:
                begin += 1
                end -=1
            
        return "".join(new_str)
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.reverseOnlyLetters(s = "ab-cd")
    assert test1 == "dc-ba"
    
    test2 = sol.reverseOnlyLetters(s = "a-bC-dEf-ghIj")
    assert test2 == "j-Ih-gfE-dCba"
    
    test3 = sol.reverseOnlyLetters(s = "Test1ng-Leet=code-Q!")
    assert test3 == "Qedo1ct-eeLg=ntse-T!"
    