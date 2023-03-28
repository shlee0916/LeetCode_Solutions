'''
https://leetcode.com/problems/minimum-cost-for-tickets/description/
'''

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day7_ticket = []
        day30_ticket = []
        cost = 0
        for day in days:
            while day7_ticket and day7_ticket[0][0] + 7 <= day:
                day7_ticket.pop(0)
            while day30_ticket and day30_ticket[0][0] + 30 <= day:
                day30_ticket.pop(0)

            day7_ticket.append((day, cost + costs[1]))
            day30_ticket.append((day, cost + costs[2]))

            cost = min(cost + costs[0], day7_ticket[0][1], day30_ticket[0][1])

        return cost
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.mincostTickets(days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15])
    print(test1, 11)
    assert test1 == 11

    test2 = sol.mincostTickets(days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs = [2, 7, 15])
    print(test2, 17)
    assert test2 == 17
