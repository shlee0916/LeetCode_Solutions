'''
https://leetcode.com/problems/longest-palindrome/
'''
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        
        length = 0
        odd_flag = False
        for key, val in cnt.items():
            if not odd_flag and val % 2 == 1:
                odd_flag = True
            length += (val // 2) * 2
            
        return length + odd_flag


if __name__ == "__main__":
    sol = Solution()

    print(sol.longestPalindrome("aa"), 2)
    print(sol.longestPalindrome("abccccdd"), 7)