'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/?envType=daily-question&envId=2024-02-24
'''

from collections import defaultdict
from heapq import heappop, heappush

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for from_city, to_city, price in flights:
            graph[from_city][to_city] = price

        heap = [(0, src, k + 1)]
        visit = [0] * n
        while heap:
            cur_price, cur_city, cur_stop = heappop(heap)
            if cur_city == dst:
                return cur_price

            if visit[cur_city] >= cur_stop:
                continue

            visit[cur_city] = cur_stop

            for next_city, price in graph[cur_city].items():
                heappush(heap, (price + cur_price, next_city, cur_stop - 1))

        return -1
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findCheapestPrice(n = 4, flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src = 0, dst = 3, k = 1)
    assert test1 == 700
    
    test2 = sol.findCheapestPrice(n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 1)
    assert test2 == 200
    
    test3 = sol.findCheapestPrice(n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 0)
    assert test3 == 500
    