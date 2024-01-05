'''
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/
'''

from heapq import heapify, heappop
from collections import Counter

from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numbers_cnt = list(Counter(arr).values())
        heapify(numbers_cnt)

        while k > 0:
            k -= heappop(numbers_cnt)

        return len(numbers_cnt) + (k < 0)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findLeastNumOfUniqueInts(arr = [5, 5, 4], k = 1)
    assert test1 == 1

    test2 = sol.findLeastNumOfUniqueInts(arr = [4, 3, 1, 1, 3, 3, 2], k = 3)
    assert test2 == 2
    