'''
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
'''

from collections import defaultdict
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 0
        check = defaultdict(int)
        
        for num in arr:
            check[num] = check[num - difference] + 1
            ans = max(ans, check[num])

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.longestSubsequence(arr = [1, 2, 3, 4], difference = 1)
    assert test1 == 4

    test2 = sol.longestSubsequence(arr = [1, 3, 5, 7], difference = 1)
    assert test2 == 1

    test3 = sol.longestSubsequence(arr = [1, 5, 7, 8, 5, 3, 4, 2, 1], difference = -2)
    assert test3 == 4
    