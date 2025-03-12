'''
https://leetcode.com/problems/longest-nice-substring/
'''

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for left in range(len(s)):
            for right in range(left + 1, len(s) + 1):
                if all(s[idx].swapcase() in s[left : right] for idx in range(left, right)):
                    ans = max(ans, s[left : right], key = len)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.longestNiceSubstring(s = "YazaAay")
    assert test1 == "aAa"
    
    test2 = sol.longestNiceSubstring(s = "Bb")
    assert test2 == "Bb"
    
    test3 = sol.longestNiceSubstring(s = "c")
    assert test3 == ""
    