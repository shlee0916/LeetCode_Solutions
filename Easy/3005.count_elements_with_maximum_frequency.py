'''
https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2024-03-08
'''

from collections import Counter

from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        max_fre = max(cnts.values())
        return sum(cnt for num, cnt in cnts.items() if cnt == max_fre)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxFrequencyElements(nums = [1, 2, 2, 3, 1, 4])
    assert test1 == 4
    
    test2 = sol.maxFrequencyElements(nums = [1, 2, 3, 4, 5])
    assert test2 == 5
    