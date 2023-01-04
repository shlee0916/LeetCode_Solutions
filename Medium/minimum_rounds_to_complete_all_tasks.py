'''
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
'''

from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks_count = Counter(tasks).values()

        if 1 in tasks_count:
            return -1

        return sum((task + 2) // 3 for task in tasks_count)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumRounds(tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4])
    print(test1, 4)
    assert test1 == 4

    test2 = sol.minimumRounds(tasks = [2, 3, 3])
    print(test2, -1)
    assert test2 == -1
    