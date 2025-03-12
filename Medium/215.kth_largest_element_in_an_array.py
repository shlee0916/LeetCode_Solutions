'''
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heappush(heap, num)

        for _ in range(len(nums) - k):
            heappop(heap)

        return heappop(heap)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    print(test1, 5)
    assert test1 == 5

    test2= sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(test2, 4)
    assert test2 == 4
