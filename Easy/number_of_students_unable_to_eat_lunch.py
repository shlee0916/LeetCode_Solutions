'''
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
'''

from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        
        total_students = len(students)
        sequence = 0

        while sequence < total_students and count[sandwiches[sequence]]:
            count[sandwiches[sequence]] -= 1
            sequence += 1

        return total_students - sequence


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countStudents(students = [1, 1, 0, 0], sandwiches = [0, 1, 0, 1])
    assert test1 == 0
    
    test2 = sol.countStudents(students = [1, 1, 1, 0, 0, 1], sandwiches = [1, 0, 0, 0, 1, 1])
    assert test2 == 3
    