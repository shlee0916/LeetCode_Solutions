'''
https://leetcode.com/problems/reorganize-string/description/
'''

from heapq import heapify, heappop, heappush
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        char_cnt = Counter(s)
        char_cnt = [(-val, key) for key, val in char_cnt.items()]
        heapify(char_cnt)

        prev_ch = ""
        prev_num = 0
        new_str = []
        while char_cnt:
            num, ch = heappop(char_cnt)
            new_str += [ch]

            if prev_num < 0:
                heappush(char_cnt, (prev_num, prev_ch))
            
            num += 1
            prev_num = num
            prev_ch = ch

        new_str = "".join(new_str)

        return new_str if len(new_str) == len(s) else ""


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.reorganizeString(s = "aab")
    assert test1 == "aba"

    test2 = sol.reorganizeString(s = "aaab")
    assert test2 == ""
    