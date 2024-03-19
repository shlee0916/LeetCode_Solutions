'''
https://leetcode.com/problems/employee-importance/
'''

from collections import defaultdict

from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        teammate = [id]
        total_imps = 0
        employee_map = defaultdict(list)
        employee_imps = {}

        for emp in employees:
            employee_map[emp.id].extend(emp.subordinates)
            employee_imps[emp.id] = emp.importance

        while teammate:
            cur_emp = teammate.pop()
            total_imps += employee_imps[cur_emp]
            teammate.extend(employee_map[cur_emp])

        return total_imps
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getImportance(employees = [Employee(1, 5, [2,3]), Employee(2, 3, []), Employee(3, 3, [])], id = 1)
    assert test1 == 11

    test2 = sol.getImportance(employees = [Employee(1, 2, [5]), Employee(5, -3, [])], id = 5)
    assert test2 == -3
    