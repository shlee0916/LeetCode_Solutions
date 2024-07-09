'''
https://leetcode.com/problems/average-waiting-time/?envType=daily-question&envId=2024-07-09
'''

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting = 0
        cur_time = 0

        for arrive_time, prepare_time in customers:
            cur_time = max(cur_time, arrive_time) + prepare_time
            total_waiting += cur_time - arrive_time

        return total_waiting / len(customers)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.averageWaitingTime(customers = [[1, 2], [2, 5], [4, 3]])
    assert test1 == 5.00000

    test2 = sol.averageWaitingTime(customers = [[5, 2], [5, 4], [10, 3], [20, 1]])
    assert test2 == 3.25000
    