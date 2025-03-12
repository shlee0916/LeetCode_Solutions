'''
https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
'''

from heapq import heapify, heappop
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap = nums
        heapify(heap)

        cnt = 0
        while heap:
            cur_val = heappop(heap)

            if cur_val <= 0:
                continue
            else:
                for idx in range(len(heap)):
                    heap[idx] -= cur_val

            cnt += 1

        return cnt


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minimumOperations(nums = [1, 5, 0, 3, 5])
    assert test1 == 3
    
    test2 = sol.minimumOperations(nums = [0])
    assert test2 == 0
    