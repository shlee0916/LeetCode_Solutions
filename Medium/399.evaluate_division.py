'''
https://leetcode.com/problems/evaluate-division/
'''

from collections import defaultdict, deque

from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (from_num, to_num), value in zip(equations, values):
            graph[from_num].append((to_num, value))
            graph[to_num].append((from_num, value ** -1))

        def dfs(from_num, to_num):
            if from_num not in graph or to_num not in graph:
                return -1.0

            que = deque([key_value for key_value in graph[from_num]])
            visit = set()
            while que:
                num, val = que.popleft()
                if num == to_num:
                    return val
                visit.add(num)
                for next_num, next_val in graph[num]:
                    if next_num not in visit:
                        que.append((next_num, val * next_val))

            return -1.0

        res = []
        for from_num, to_num in queries:
            res.append(dfs(from_num, to_num))

        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.calcEquation(equations = [["a", "b"], ["b", "c"]], values = [2.0, 3.0], queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    assert test1 == [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

    test2 = sol.calcEquation(equations = [["a", "b"], ["b", "c"], ["bc", "cd"]], values = [1.5, 2.5, 5.0], queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]])
    assert test2 == [3.75000, 0.40000, 5.00000, 0.20000]

    test3 = sol.calcEquation(equations = [["a", "b"]], values = [0.5], queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]])
    assert test3 == [0.50000, 2.00000, -1.00000, -1.00000]
    