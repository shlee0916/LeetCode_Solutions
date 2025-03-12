'''
https://leetcode.com/problems/smallest-number-in-infinite-set/description/
'''

from heapq import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self.next_num = 1
        self.check = set()
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            small_num = heappop(self.heap)
            self.check.remove(small_num)
        else:
            small_num = self.next_num
            self.next_num += 1
        
        return small_num

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.check:
            self.check.add(num)
            heappush(self.heap, num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

if __name__ == "__main__":
    si = SmallestInfiniteSet()

    assert 1 == si.popSmallest()
    assert 2 == si.popSmallest()

    si.addBack(1)
    si.addBack(100)
    assert 1 == si.popSmallest()
    assert 3 == si.popSmallest()
