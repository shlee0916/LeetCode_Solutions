'''
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
'''

from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        road_map = defaultdict(list)
        
        for depart, arrive in roads:
            road_map[depart].append(arrive)
            road_map[arrive].append(depart)

        self.total_fuel = 0

        def dfs(cur_city, prev_city, people = 1):
            for next_city in road_map[cur_city]:
                if next_city == prev_city:
                    continue

                people += dfs(next_city, cur_city)

            self.total_fuel += int(ceil(people / seats)) if cur_city else 0

            return people

        dfs(0, 0)

        return self.total_fuel
            
            
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minimumFuelCost(roads = [[0, 1], [0, 2], [0, 3]], seats = 5)
    assert test1 == 3
    
    test2 = sol.minimumFuelCost(roads = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats = 2)
    assert test2 == 7
    
    test3 = sol.minimumFuelCost(roads = [], seats = 1)
    assert test3 == 0
    