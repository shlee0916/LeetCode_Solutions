'''
https://leetcode.com/problems/number-of-good-pairs/description/
'''

from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_cnt = Counter(nums)

        ans = 0
        for value in num_cnt.values():
            ans += value * (value - 1) // 2

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numIdenticalPairs(nums = [1, 2, 3, 1, 1, 3])
    assert test1 == 4
    
    test2 = sol.numIdenticalPairs(nums = [1, 1, 1, 1])
    assert test2 == 6
    
    test3 = sol.numIdenticalPairs(nums = [1, 2, 3])
    assert test3 == 0
    