'''
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/
'''

from collections import Counter
from heapq import heappop, heappush

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for num in nums:
            heappush(heap, num)

            if len(heap) > k:
                heappop(heap)

        num_cnt = Counter(heap)

        ans = []
        for num in nums:
            if num_cnt[num] > 0:
                num_cnt[num] -= 1
                ans.append(num)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxSubsequence(nums = [2, 1, 3, 3], k = 2)
    assert test1 == [3, 3]
    
    test2 = sol.maxSubsequence(nums = [-1, -2, 3, 4], k = 3)
    assert test2 == [-1, 3, 4]
    
    test3 = sol.maxSubsequence(nums = [3, 4, 3, 3], k = 2)
    assert test3 == [3, 4]
    