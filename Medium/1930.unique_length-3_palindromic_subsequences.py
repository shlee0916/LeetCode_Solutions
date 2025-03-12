'''
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2023-11-14
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        seen = set()
        for ch in set(s):
            left, right = s.find(ch), s.rfind(ch)

            if right - left > 1:
                for idx in range(left + 1, right):
                    seen.add(s[left] + s[idx] + s[right])

        return len(seen)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countPalindromicSubsequence(s = "aabca")
    assert test1 == 3

    test2 = sol.countPalindromicSubsequence(s = "adc")
    assert test2 == 0

    test3 = sol.countPalindromicSubsequence(s = "bbcbaba")
    assert test3 == 4
    