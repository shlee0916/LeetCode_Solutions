'''
https://leetcode.com/problems/longest-repeating-character-replacement/
'''

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        left = 0

        for right in range(len(s)):
            cnt[s[right]] += 1
            max_cnt = max(cnt.values())
            while right - left + 1 - max_cnt > k:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.characterReplacement(s = "ABAB", k = 2)
    assert test1 == 4

    test2 = sol.characterReplacement(s = "AABABBA", k = 1)
    assert test2 == 4
    