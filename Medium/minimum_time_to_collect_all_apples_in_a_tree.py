'''
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
'''

from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(cur, parents):
            cnt_path = 0

            for child in graph[cur]:
                if child != parents:
                    cnt_path += dfs(child, cur)

            if cnt_path or hasApple[cur]:
                return cnt_path + 2

            return cnt_path
        
        graph = {}
        for ed, ge in edges:
            if ed in graph:
                graph[ed].append(ge)
            else:
                graph[ed] = [ge]

            if ge in graph:
                graph[ge].append(ed)
            else:
                graph[ge] = [ed]

        return max(dfs(0, -1) - 2, 0)
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minTime(n = 7, edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple = [False, False, True, False, True, True, False])
    print(test1, 8)
    assert test1 == 8

    test2 = sol.minTime(n = 7, edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple = [False, False, True, False, False, True, False])
    print(test2, 6)
    assert test2 == 6

    test3 = sol.minTime(n = 7, edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple = [False, False, False, False, False, False, False])
    print(test3, 0)
    assert test3 == 0
