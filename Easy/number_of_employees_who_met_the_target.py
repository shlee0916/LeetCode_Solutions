'''
https://leetcode.com/problems/number-of-employees-who-met-the-target/
'''

from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        return sum(hour >= target for hour in hours)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numberOfEmployeesWhoMetTarget(hours = [0, 1, 2, 3, 4], target = 2)
    assert test1 == 3

    test2 = sol.numberOfEmployeesWhoMetTarget(hours = [5, 1, 4, 2, 2], target = 6)
    assert test2 == 0
    