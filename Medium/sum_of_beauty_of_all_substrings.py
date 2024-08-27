'''
https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
'''

from collections import defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for start in range(len(s)):
            freq = defaultdict(int)
            for end in range(start, len(s)):
                freq[s[end]] += 1
                ans += max(freq.values()) - min(freq.values())

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.beautySum(s = "aabcb")
    assert test1 == 5

    test2 = sol.beautySum(s = "aabcbaa")
    assert test2 == 17
    