'''
https://leetcode.com/problems/most-profit-assigning-work/?envType=daily-question&envId=2024-06-18
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0

        profit_diff = []
        for pro, diff in zip(profit, difficulty):
            heappush(profit_diff, (-pro, diff))

        worker.sort(reverse = True)
        worker_idx = 0
        while profit_diff and worker_idx < len(worker):
            cur_pro, cur_diff = heappop(profit_diff)

            while worker_idx < len(worker) and worker[worker_idx] >= cur_diff:
                ans -= cur_pro
                worker_idx += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxProfitAssignment(difficulty = [2, 4, 6, 8, 10], profit = [10, 20, 30, 40, 50], worker = [4, 5, 6, 7])
    assert test1 == 100

    test2 = sol.maxProfitAssignment(difficulty = [85, 47, 57], profit = [24, 66, 99], worker = [40, 25, 25])
    assert test2 == 0
    