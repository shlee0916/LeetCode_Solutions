'''
https://leetcode.com/problems/majority-element/
'''
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        eles = cnt.most_common()
        
        return eles[0][0]


if __name__ == "__main__":
    sol = Solution()

    print(sol.majorityElement([2, 3, 2]))