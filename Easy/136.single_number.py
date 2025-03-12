'''
https://leetcode.com/problems/single-number/
'''
from typing import List
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        return count.most_common()[-1][0]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.singleNumber([4, 1, 2, 1, 2]), 4)