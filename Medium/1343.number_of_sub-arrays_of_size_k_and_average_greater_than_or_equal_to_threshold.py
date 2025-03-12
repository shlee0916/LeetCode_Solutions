'''
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
'''

from itertools import accumulate
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        acc = [0] + list(accumulate(arr))
        res = 0
        for idx in range(len(arr) - k + 1):
            if acc[idx + k] - acc[idx] >= k * threshold:
                res += 1

        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numOfSubarrays(arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4)
    print(test1, 3)
    assert test1 == 3
    
    test2 = sol.numOfSubarrays(arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k = 3, threshold = 5)
    print(test2, 6)
    assert test2 == 6
