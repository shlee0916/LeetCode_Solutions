'''
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
'''

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        subarray_len = len(cardPoints) - k
        
        min_subarray = sum(cardPoints[:subarray_len])
        cur = min_subarray
        for idx in range(len(cardPoints) - subarray_len):
            cur += cardPoints[idx + subarray_len] - cardPoints[idx]
            min_subarray = min(min_subarray, cur)

        return sum(cardPoints) - min_subarray
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxScore(cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3)
    assert test1 == 12

    test2 = sol.maxScore(cardPoints = [2, 2, 2], k = 2)
    assert test2 == 4

    test3 = sol.maxScore(cardPoints = [9, 7, 7, 9, 7, 7, 9], k = 7)
    assert test3 == 55
