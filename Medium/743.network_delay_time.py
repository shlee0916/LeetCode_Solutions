'''
https://leetcode.com/problems/network-delay-time/description/
'''

from collections import defaultdict
from heapq import heappop, heappush

from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        heap = [(0, k)]
        elapsed_time = {}

        for depart, arrive, time in times:
            graph[depart][arrive] = time

        while heap:
            cur_time, cur_node = heappop(heap)
            if cur_node not in elapsed_time:
                elapsed_time[cur_node] = cur_time
            
                for next_node, time in graph[cur_node].items():
                    heappush(heap, (cur_time + time, next_node))

        return max(elapsed_time.values()) if len(elapsed_time) == n else -1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.networkDelayTime(times = [[2, 1, 1], [2, 3, 1], [3, 4,1]], n = 4, k = 2)
    assert test1 == 2
    
    test2 = sol.networkDelayTime(times = [[1, 2, 1]], n = 2, k = 1)
    assert test2 == 1
    
    test3 = sol.networkDelayTime(times = [[1, 2 ,1]], n = 2, k = 2)
    assert test3 == -1
    