'''
https://leetcode.com/problems/ipo/description/
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = sorted(zip(profits, capital), key = lambda x: x[1])
        cur_w = w

        idx = 0
        for _ in range(k):
            while idx < len(projects) and projects[idx][1] <= cur_w:
                heappush(heap, -projects[idx][0])
                idx += 1

            if heap:
                cur_w -= heappop(heap)

        return cur_w


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findMaximizedCapital(k = 2, w = 0, profits = [1, 2, 3], capital = [0, 1, 1])
    assert test1 == 4
    
    test2 = sol.findMaximizedCapital(k = 3, w = 0, profits = [1, 2, 3], capital = [0, 1, 2])
    assert test2 == 6
    