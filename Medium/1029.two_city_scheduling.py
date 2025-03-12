'''
https://leetcode.com/problems/two-city-scheduling/description/
'''

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_a_cost = 0
        cost_diff = []
        for a_cost, b_cost in costs:
            total_a_cost += a_cost
            cost_diff.append(b_cost - a_cost)

        return total_a_cost + sum(sorted(cost_diff)[:len(costs) // 2])
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.twoCitySchedCost(costs = [[10, 20], [30, 200], [400, 50], [30, 20]])
    print(test1, 110)
    assert test1 == 110

    test2 = sol.twoCitySchedCost(costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]])
    print(test2, 1859)
    assert test2 == 1859

    test3 = sol.twoCitySchedCost(costs = [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]])
    print(test3, 3086)
    assert test3 == 3086
    