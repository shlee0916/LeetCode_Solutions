'''
https://leetcode.com/problems/left-and-right-sum-differences/description/
'''

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = 0
        suffix = sum(nums)
        for ele in nums:
            prefix += ele
            ans.append(abs(prefix - suffix))
            suffix -= ele

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.leftRightDifference(nums = [10, 4, 8, 3])
    assert test1 == [15, 1, 11, 22]
    
    test2 = sol.leftRightDifference(nums = [1])
    assert test2 == [0]
    