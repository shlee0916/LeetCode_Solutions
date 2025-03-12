'''
https://leetcode.com/problems/construct-string-with-repeat-limit/?envType=daily-question&envId=2024-12-17
'''

from collections import Counter
from heapq import heapify, heappush, heappop


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(ch), num) for ch, num in Counter(s).items()]
        heapify(heap)
        
        ans = []
        while heap:
            ch, num = heappop(heap)

            if ans and ans[-1] == ch:
                if not heap:
                    break

                next_ch, next_num = heappop(heap)
                ans.append(next_ch)
                if next_num - 1 > 0:
                    heappush(heap, (next_ch, next_num - 1))
                heappush(heap, (ch, num))

            else:
                ans.extend([ch] * min(num, repeatLimit))
                if num - repeatLimit > 0:
                    heappush(heap, (ch, num - repeatLimit))

        return "".join(chr(-ch) for ch in ans)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.repeatLimitedString(s = "cczazcc", repeatLimit = 3)
    assert test1 == "zzcccac"

    test2 = sol.repeatLimitedString(s = "aababab", repeatLimit = 2)
    assert test2 == "bbabaa"
