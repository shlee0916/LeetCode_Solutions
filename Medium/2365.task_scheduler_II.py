'''
https://leetcode.com/problems/task-scheduler-ii/description/
'''

from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        prev_tasks = {}
        days = 0

        for task in tasks:
            days += 1

            if task in prev_tasks and days - prev_tasks[task] <= space:
                days += space - (days - prev_tasks[task]) + 1

            prev_tasks[task] = days

        return days
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.taskSchedulerII(tasks = [1, 2, 1, 2, 3, 1], space = 3)
    assert test1 == 9
    
    test2 = sol.taskSchedulerII(tasks = [5, 8, 8, 5], space = 2)
    assert test2 == 6
    