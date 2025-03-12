'''
https://leetcode.com/problems/seat-reservation-manager/description/?envType=daily-question&envId=2023-11-06
'''

from heapq import heapify, heappop, heappush


class SeatManager:

    def __init__(self, n: int):
        self.heap = [num for num in range(n)]
        heapify(self.heap)


    def reserve(self) -> int:
        return heappop(self.heap) + 1 if self.heap else None
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap, seatNumber - 1)
        

if __name__ == "__main__":
    sm = SeatManager(n = 5)

    assert sm.reserve() == 1
    assert sm.reserve() == 2
    sm.unreserve(2)
    assert sm.reserve() == 2
    assert sm.reserve() == 3
    assert sm.reserve() == 4
    assert sm.reserve() == 5
    assert sm.reserve() == None
    sm.unreserve(5)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
