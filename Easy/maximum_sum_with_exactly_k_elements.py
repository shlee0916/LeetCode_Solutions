'''
https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/
'''

from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + k * (k - 1) // 2


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maximizeSum(nums = [1, 2, 3, 4, 5], k = 3)
    assert test1 == 18
    
    test2 = sol.maximizeSum(nums = [5, 5, 5], k = 2)
    assert test2 == 11
    