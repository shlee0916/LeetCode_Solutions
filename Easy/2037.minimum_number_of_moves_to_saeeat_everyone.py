'''
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
'''

from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans = 0
        for seat, student in zip(sorted(seats), sorted(students)):
            ans += abs(seat - student)

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minMovesToSeat(seats = [3, 1, 5], students = [2, 7, 4])
    assert test1 == 4
    
    test2 = sol.minMovesToSeat(seats = [4, 1, 5, 9], students = [1, 3, 2, 6])
    assert test2 == 7
    
    test3 = sol.minMovesToSeat(seats = [2,2 ,6 ,6 ], students = [1, 3, 2, 6])
    assert test3 == 4
    