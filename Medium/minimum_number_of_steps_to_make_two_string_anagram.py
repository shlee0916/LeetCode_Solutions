'''
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
'''

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt = Counter(s)
        cnt = 0
        for ch in t:
            if s_cnt[ch] > 0:
                s_cnt[ch] -= 1
            else:
                cnt += 1

        return cnt


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minSteps(s = "bab", t = "aba")
    assert test1 == 1
    
    test2 = sol.minSteps(s = "leetcode", t = "practice")
    assert test2 == 5
    
    test3 = sol.minSteps(s = "anagram", t = "mangaar")
    assert test3 == 0
    