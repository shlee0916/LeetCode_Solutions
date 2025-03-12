'''
https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/?envType=daily-question&envId=2023-12-31
'''

from collections import defaultdict


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        ch_idxs = defaultdict(list)

        for idx, ch in enumerate(s):
            ch_idxs[ch].append(idx)

        for idxs in ch_idxs.values():
            ans = max(ans, max(idxs) - min(idxs) - 1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxLengthBetweenEqualCharacters(s = "aa")
    assert test1 == 0
    
    test2 = sol.maxLengthBetweenEqualCharacters(s = "abca")
    assert test2 == 2
    
    test3 = sol.maxLengthBetweenEqualCharacters(s = "cbzxy")
    assert test3 == -1
    