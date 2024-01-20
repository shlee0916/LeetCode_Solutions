'''
https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(ch.lower() for ch in s if ch.isalpha() or ch.isdigit())

        return new_s == new_s[::-1]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isPalindrome(s = "A man, a plan, a canal: Panama")
    assert test1 == True
    
    test2 = sol.isPalindrome(s = "race a car")
    assert test2 == False
    
    test3 = sol.isPalindrome(s = " ")
    assert test3 == True
    