'''
https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/?envType=daily-question&envId=2024-10-12
'''

from heapq import heappop, heappush

from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        for left, right in sorted(intervals):
            if heap and heap[0] < left:
                heappop(heap)
            heappush(heap, right)

        return len(heap)
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minGroups(intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]])
    assert test1 == 3

    test2 = sol.minGroups(intervals = [[1, 3], [5, 6], [8, 10], [11, 13]])
    assert test2 == 1
    