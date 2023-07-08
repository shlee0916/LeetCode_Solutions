'''
https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/description/
'''

from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.ans = 0

        def dfs(node_idx):
            if node_idx >= len(cost):
                return 0

            left_cost, right_cost = dfs(2 * node_idx + 1), dfs(2 * node_idx + 2)
            self.ans += abs(left_cost - right_cost)

            return cost[node_idx] + max(left_cost, right_cost)

        dfs(0)

        return self.ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minIncrements(n = 7, cost = [1, 5 ,2 ,2 ,3 ,3 ,1 ])
    assert test1 == 6
    
    test2 = sol.minIncrements(n = 3, cost = [5, 3, 3])
    assert test2 == 0
    