'''
https://leetcode.com/problems/bus-routes/description/?envType=daily-question&envId=2023-11-12
'''

from collections import defaultdict, deque

from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        bus_routes = defaultdict(set)
        for bus_num, stops in enumerate(routes):
            for stop in stops:
                bus_routes[stop].add(bus_num)

        que = deque([(source, 0)])
        seen_stop = set()
        seen_bus = set()
        while que:
            cur_stop, bus_cnt = que.popleft()
            if cur_stop == target:
                return bus_cnt

            for bus_num in bus_routes[cur_stop]:
                if bus_num not in seen_bus:
                    seen_bus.add(bus_num)
                    
                    for next_stop in routes[bus_num]:
                        if next_stop not in seen_stop:
                            seen_stop.add(next_stop)
                            que.append((next_stop, bus_cnt + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numBusesToDestination(routes = [[1, 2, 7], [3, 6, 7]], source = 1, target = 6)
    assert test1 == 2
    
    test2 = sol.numBusesToDestination(routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source = 15, target = 12)
    assert test2 == -1
    