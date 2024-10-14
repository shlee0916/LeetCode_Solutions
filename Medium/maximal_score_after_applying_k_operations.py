'''
https://leetcode.com/problems/maximal-score-after-applying-k-operations/?envType=daily-question&envId=2024-10-14
'''

from heapq import heappush, heappop
from math import ceil

from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        heap = []
        for num in nums:
            heappush(heap, -num)

        for _ in range(k):
            num = heappop(heap)
            ans -= num
            heappush(heap, -ceil(-num / 3))

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxKelements(nums = [10, 10, 10, 10, 10], k = 5)
    assert test1 == 50

    test2 = sol.maxKelements(nums = [1, 10, 3, 3, 3], k = 3)
    assert test2 == 17
    