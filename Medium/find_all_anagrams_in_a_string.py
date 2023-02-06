'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/892468615/
'''

from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_cnt = defaultdict(int)
        result = []
        length_s = len(s)
        length_p = len(p)

        if length_p > length_s:
            return []

        for p_char in p:
            char_cnt[p_char] += 1

        for idx in range(length_p - 1):
            if s[idx] in char_cnt:
                char_cnt[s[idx]] -= 1

        for idx in range(-1, length_s - length_p + 1):
            if idx > -1 and s[idx] in char_cnt:
                char_cnt[s[idx]] += 1
            if idx + length_p < length_s and s[idx + length_p] in char_cnt:
                char_cnt[s[idx + length_p]] -= 1

            if all(val == 0 for val in char_cnt.values()):
                result.append(idx + 1)

        return result


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findAnagrams(s = "cbaebabacd", p = "abc")
    print(test1, [0, 6])
    assert test1 == [0, 6]

    test2 = sol.findAnagrams(s = "abab", p = "ab")
    print(test2, [0, 1, 2])
    assert test2 == [0, 1, 2]
    