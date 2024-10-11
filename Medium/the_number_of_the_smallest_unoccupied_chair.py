'''
https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/?envType=daily-question&envId=2024-10-11
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arr_leav_time = []

        for idx, (arr, leav) in enumerate(times):
            arr_leav_time.append((arr, 1, idx))
            arr_leav_time.append((leav, 0, idx))

        cur_chair = 0
        chairs = []
        seating_map = {}
        for time, seat_up, idx in sorted(arr_leav_time):
            if seat_up:
                if chairs:
                    seat_num = heappop(chairs)
                
                else:
                    seat_num = cur_chair
                    cur_chair += 1
                
                if idx == targetFriend:
                    return seat_num

                seating_map[idx] = seat_num

            else:
                heappush(chairs, seating_map[idx])


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.smallestChair(times = [[1, 4], [2, 3], [4, 6]], targetFriend = 1)
    assert test1 == 1

    test2 = sol.smallestChair(times = [[3, 10], [1, 5], [2, 6]], targetFriend = 0)
    assert test2 == 2
    