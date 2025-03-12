'''
https://leetcode.com/problems/all-paths-from-source-to-target/description/
'''

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur_node: int, path: List[int], target: int, res: List[List[int]], graph: List[List[int]],):
            if cur_node == target:
                res.append(path + [cur_node])
                return

            for next_node in graph[cur_node]:
                dfs(next_node, path + [cur_node], target, res, graph)


        res = []
        dfs(0, [], len(graph) - 1, res, graph)
        
        return res


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.allPathsSourceTarget(graph = [[1, 2], [3], [3], []])
    print(test1, [[0, 1, 3], [0, 2, 3]])
    assert test1 == [[0, 1, 3], [0, 2, 3]]
    
    test2 = sol.allPathsSourceTarget(graph = [[4, 3, 1], [3, 2, 4], [3], [4], []])
    print(test2, [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]])
    assert test2 == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    