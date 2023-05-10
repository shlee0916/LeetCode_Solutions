'''
https://leetcode.com/problems/task-scheduler/description/
'''

from collections import Counter
from heapq import heappush, heappop

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        work_cnt = Counter(tasks)
        min_heap = []

        for work, cnt in work_cnt.items():
            heappush(min_heap, (-cnt, work))

        total_time = 0
        while min_heap:
            left_works = []
            idle_time = 0

            while idle_time <= n:
                total_time += 1

                if min_heap:
                    left_cnt, work = heappop(min_heap)

                    left_cnt += 1
                    if left_cnt < 0:
                        left_works.append((left_cnt, work))

                if not min_heap and not left_works:
                    break
                else:
                    idle_time += 1
            
            for left in left_works:
                heappush(min_heap, left)

        return total_time


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.leastInterval(tasks = ["A", "A", "A", "B", "B", "B"], n = 2)
    assert test1 == 8

    test2 = sol.leastInterval(tasks = ["A", "A", "A", "B", "B", "B"], n = 0)
    assert test2 == 6

    test3 = sol.leastInterval(tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n = 2)
    assert test3 == 16
    