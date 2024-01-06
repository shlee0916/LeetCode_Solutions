'''
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/description/
'''

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt = Counter(s)
        t_cnt = Counter(t)

        return sum(abs(s_cnt[ch] - t_cnt[ch]) for ch in "abcdefghijklmnopqrstuvwxyz")


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minSteps(s = "leetcode", t = "coats")
    assert test1 == 7
    
    test2 = sol.minSteps(s = "night", t = "thing")
    assert test2 == 0
    