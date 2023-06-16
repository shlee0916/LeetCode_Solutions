'''
https://leetcode.com/problems/construct-k-palindrome-strings/description/
'''

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        all_chs = Counter(s)

        odd_chs = 0

        for ch, num in all_chs.items():
            if num % 2 != 0:
                odd_chs += 1

        return odd_chs <= k <= len(s)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.canConstruct(s = "annabelle", k = 2)
    assert test1 == True

    test2 = sol.canConstruct(s = "leetcode", k = 3)
    assert test2 == False

    test3 = sol.canConstruct(s = "true", k = 4)
    assert test3 == True
    