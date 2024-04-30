'''
https://leetcode.com/problems/palindromic-substrings/
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        ans = 0

        for idx in range(2 * length - 1):
            left = idx // 2
            right = (idx + 1) // 2

            while left >= 0 and right < length and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countSubstrings(s = "abc")
    assert test1 == 3

    test2 = sol.countSubstrings(s = "aaa")
    assert test2 == 6
    