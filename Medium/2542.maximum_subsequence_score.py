'''
https://leetcode.com/problems/maximum-subsequence-score/description/
'''

from heapq import heappush, heappop
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = zip(nums1, nums2)
        pairs = sorted(pairs, key = lambda pair: -pair[1])

        heap = []
        total = 0
        res = 0
        for num1, num2 in pairs:
            heappush(heap, num1)
            total += num1
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                res = max(res, total * num2)

        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxScore(nums1 = [1, 3, 3, 2], nums2 = [2, 1, 3, 4], k = 3)
    assert test1 == 12

    test2 = sol.maxScore(nums1 = [4, 2, 3, 1, 1], nums2 = [7, 5, 10, 9, 6], k = 1)
    assert test2 == 30
    