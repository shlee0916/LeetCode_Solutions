'''
https://leetcode.com/problems/k-th-smallest-prime-fraction/?envType=daily-question&envId=2024-05-10
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        length = len(arr)

        for start_idx in range(length):
            for end_idx in range(start_idx + 1, length):
                fraction = (arr[start_idx] / arr[end_idx], (arr[start_idx], arr[end_idx]))
                heappush(heap, fraction)

        for _ in range(k - 1):
            heappop(heap)

        return heappop(heap)[1]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.kthSmallestPrimeFraction(arr = [1, 2, 3, 5], k = 3)
    assert test1 == (2, 5)
    
    test2 = sol.kthSmallestPrimeFraction(arr = [1, 7], k = 1)
    assert test2 == (1, 7)
    