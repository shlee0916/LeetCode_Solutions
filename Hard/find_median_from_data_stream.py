'''
https://leetcode.com/problems/find-median-from-data-stream/description/
'''
from heapq import *


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, -num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, num))


    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] - self.min_heap[0]) / 2
        else:
            return (self.max_heap[0])


if __name__ == "__main__":
    mf = MedianFinder()
    
    mf.addNum(1)
    mf.addNum(2)
    
    assert mf.findMedian() == 1.5
    
    mf.addNum(3)
    
    assert mf.findMedian() == 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()