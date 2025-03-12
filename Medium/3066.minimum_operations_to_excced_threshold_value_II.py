'''
https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?envType=daily-question&envId=2025-02-13
'''

from heapq import heapify, heappop, heappush

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heap = nums[:]
        heapify(heap)

        while heap[0] < k:
            smallest = heappop(heap)
            small = heappop(heap)

            heappush(heap, smallest * 2 + small)
            ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minOperations(nums = [2, 11, 10, 1, 3], k = 10)
    assert test1 == 2

    test2 = sol.minOperations(nums = [1, 1, 2, 4, 9], k = 20)
    assert test2 == 4