'''
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
'''

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_found = max_found = False
        start = min_start = max_start = 0

        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                min_found = False
                max_found = False
                start = idx + 1

            if num == minK:
                min_found = True
                min_start = idx

            if num == maxK:
                max_found = True
                max_start = idx

            if min_found and max_found:
                res += min(min_start, max_start) - start + 1

        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countSubarrays(nums = [1, 3, 5, 2, 7, 5], minK = 1, maxK = 5)
    print(test1, 2)
    assert test1 == 2
    
    test2 = sol.countSubarrays(nums = [1, 1, 1, 1], minK = 1, maxK = 1)
    print(test2, 10)
    assert test2 == 10
    