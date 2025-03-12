'''
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
'''

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.average(salary = [4000, 3000, 1000, 2000])
    assert test1 == 2500.00000
    
    test2 = sol.average(salary = [1000, 2000, 3000])
    assert test2 == 2000.00000
    