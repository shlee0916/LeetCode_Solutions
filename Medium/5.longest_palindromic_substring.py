'''
https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for idx in range(len(s)):
            odd = self._palindrome(idx, idx, s)
            even = self._palindrome(idx, idx + 1, s)
            
            ans = max(odd, even, ans, key = len)
            
        return ans
    
            
    def _palindrome(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return s[l + 1 : r]


if __name__ == "__main__":
    sol = Solution()

    print(sol.longestPalindrome("babad"), "bab")
    print(sol.longestPalindrome("cbbd"), "bb")