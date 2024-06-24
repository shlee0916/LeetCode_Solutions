'''
https://leetcode.com/problems/kth-largest-element-in-a-stream/
'''

from heapq import heapify, heappop, heappush, heapreplace

from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pque = nums[:]
        heapify(self.pque)
        while len(self.pque) > k:
            heappop(self.pque)
        

    def add(self, val: int) -> int:
        if len(self.pque) < self.k:
            heappush(self.pque, val)
        elif val > self.pque[0]:
            heapreplace(self.pque, val)

        return self.pque[0]


if __name__ == "__main__":
    kl = KthLargest(k = 3, nums = [4, 5, 8, 2])

    assert 4 == kl.add(3)
    assert 5 == kl.add(5)
    assert 5 == kl.add(10)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)