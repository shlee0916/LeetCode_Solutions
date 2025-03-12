'''
https://leetcode.com/problems/palindrome-number/
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isPalindrome(123))
    print(sol.isPalindrome(121))