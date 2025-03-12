'''
https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
'''

from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        pre = 0
        for num in arr:
            pre = min(pre + 1, num)

        return pre


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maximumElementAfterDecrementingAndRearranging(arr = [2, 2, 1, 2, 1])
    assert test1 == 2
    
    test2 = sol.maximumElementAfterDecrementingAndRearranging(arr = [100, 1, 1000])
    assert test2 == 3
    
    test3 = sol.maximumElementAfterDecrementingAndRearranging(arr = [1, 2, 3, 4, 5])
    assert test3 == 5
    