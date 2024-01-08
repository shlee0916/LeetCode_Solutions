'''
https://leetcode.com/problems/longest-happy-string/description/
'''

from heapq import heappush, heappop, heapreplace


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []

        for cnt, token in (-a, "a"), (-b, "b"), (-c, "c"):
            if cnt != 0:
                heappush(max_heap, (cnt, token)) 

        ans = []
        while max_heap:
            cnt, token = heappop(max_heap)

            if len(ans) > 1 and ans[-2] == ans[-1] == token:
                if not max_heap:
                    break
                cnt, token = heapreplace(max_heap, (cnt, token))

            ans.append(token)
            if cnt + 1 < 0:
                heappush(max_heap, (cnt + 1, token))

        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.longestDiverseString(a = 1, b = 1, c = 7)
    assert test1 == "ccaccbcc"

    test2 = sol.longestDiverseString(a = 7, b = 1, c = 0)
    assert test2 == "aabaa"
    