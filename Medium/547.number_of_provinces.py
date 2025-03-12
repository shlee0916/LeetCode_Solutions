'''
https://leetcode.com/problems/number-of-provinces/description/
'''

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_map = {}
        for idx, city in enumerate(isConnected):
            city_map[idx] = [way_idx for way_idx, way in enumerate(city) if way and way_idx != idx]

        visit = set()
        provinces = 0
        for city in city_map:
            if city not in visit:
                stack = [city]
                while stack:
                    cur_city = stack.pop()
                    visit.add(cur_city)
                    for next_city in city_map[cur_city]:
                        if next_city not in visit:
                            stack.append(next_city)

                provinces += 1
        
        return provinces


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findCircleNum(isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    assert test1 == 2
    
    test2 = sol.findCircleNum(isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert test2 == 3
    