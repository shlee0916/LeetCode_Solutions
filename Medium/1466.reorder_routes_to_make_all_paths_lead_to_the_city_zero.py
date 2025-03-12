'''
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
'''

from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = defaultdict(dict)
        for start, end in connections:
            roads[start][end] = 1
            roads[end][start] = -1

        visit = set()
        reorder_cnt = 0
        for city in range(n):
            if city not in visit:
                
                stack = [city]
                while stack:
                    cur_city = stack.pop()
                    visit.add(cur_city)
                    
                    for next_city in roads[cur_city].keys():

                        if next_city not in visit:
                            stack.append(next_city)
                            if roads[cur_city][next_city] == 1:
                                reorder_cnt += 1

        return reorder_cnt


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minReorder(n = 6, connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
    print(test1, 3)
    assert test1 == 3

    test2 = sol.minReorder(n = 5, connections = [[1, 0], [1, 2], [3, 2], [3, 4]])
    print(test2, 2)
    assert test2 == 2

    test3 = sol.minReorder(n = 3, connections = [[1, 0], [2, 0]])
    print(test3, 0)
    assert test3 == 0
