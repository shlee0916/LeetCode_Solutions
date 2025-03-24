'''
https://leetcode.com/problems/count-days-without-meetings/?envType=daily-question&envId=2025-03-24
'''

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])

        ans = meetings[0][0] - 1

        for idx in range(1, len(meetings)):
            if meetings[idx - 1][1] >= meetings[idx][0]:
                if meetings[idx - 1][1] > meetings[idx][1]:
                    meetings[idx][1] = meetings[idx - 1][1]

            else:
                day_gap = meetings[idx][0] - meetings[idx - 1][1]
                ans += day_gap - 1

        ans += days - meetings[-1][1]

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countDays(days = 10, meetings = [[5, 7], [1, 3], [9, 10]])
    assert test1 == 2

    test2 = sol.countDays(days = 5, meetings = [[2, 4], [1, 3]])
    assert test2 == 1

    test3 = sol.countDays(days = 6, meetings = [[1, 6]])
    assert test3 == 0
    