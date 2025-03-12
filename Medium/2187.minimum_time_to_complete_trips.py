'''
https://leetcode.com/problems/minimum-time-to-complete-trips/description/
'''

from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips

        while left < right:
            mid = (left + right) // 2

            if sum(mid // t for t in time) < totalTrips:
                left = mid + 1
            else:
                right = mid

        return left
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumTime(time = [1, 2, 3], totalTrips = 5)
    print(test1, 3)
    assert test1 == 3

    test2 = sol.minimumTime(time = [2], totalTrips = 1)
    print(test2, 2)
    assert test2 == 2
