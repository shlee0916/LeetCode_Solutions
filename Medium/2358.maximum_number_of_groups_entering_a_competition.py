'''
https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
'''

from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        num_people = len(grades)
        ans = 0

        while num_people >= ans + 1:
            ans += 1
            num_people -= ans

        return ans 


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maximumGroups(grades = [10, 6, 12, 7, 3, 5])
    assert test1 == 3
    
    test2 = sol.maximumGroups(grades = [8, 8])
    assert test2 == 1
    