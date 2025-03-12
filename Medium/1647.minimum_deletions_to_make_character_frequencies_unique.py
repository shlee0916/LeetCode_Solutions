'''
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/?envType=daily-question&envId=2023-09-12
'''

from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        ch_cnt = Counter(s)
        ans = 0
        used = set()

        for ch, cnt in ch_cnt.items():
            while cnt > 0 and cnt in used:
                cnt -= 1
                ans += 1
            used.add(cnt)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minDeletions(s = "aab")
    assert test1 == 0

    test2 = sol.minDeletions(s = "aaabbbcc")
    assert test2 == 2

    test3 = sol.minDeletions(s = "ceabaacb")
    assert test3 == 2
    