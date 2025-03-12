'''
https://leetcode.com/problems/time-needed-to-inform-all-employees/description/
'''

from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(employee):
            ans = 0
            for subord in employee_tree[employee]:
                ans = max(ans, dfs(subord) + informTime[employee])

            return ans

        employee_tree = defaultdict(list)
        for subord, head in enumerate(manager):
            employee_tree[head].append(subord)

        return dfs(headID)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0])
    assert test1 == 0
    
    test2 = sol.numOfMinutes(n = 6, headID = 2, manager = [2, 2, -1, 2, 2, 2], informTime = [0, 0, 1, 0, 0, 0])
    assert test2 == 1
    