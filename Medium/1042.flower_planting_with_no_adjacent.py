'''
https://leetcode.com/problems/flower-planting-with-no-adjacent/
'''

from collections import defaultdict

from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for garden_from, garden_to in paths:
            graph[garden_from - 1].append(garden_to - 1)
            graph[garden_to - 1].append(garden_from - 1)

        res = [0] * n
        for garden in range(n):
            planted_flowers = [res[near_garden] for near_garden in graph[garden]]
            left_flowers = {1, 2, 3, 4} - set(planted_flowers)
            res[garden] = left_flowers.pop()
        
        return res
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.gardenNoAdj(n = 3, paths = [[1, 2], [2, 3], [3, 1]])
    assert test1 == [1, 2, 3]

    test2 = sol.gardenNoAdj(n = 4, paths = [[1, 2], [3, 4]])
    assert test2 == [1, 2, 1, 2]

    test3 = sol.gardenNoAdj(n = 4, paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]])
    assert test3 == [1, 2, 3, 4]
    