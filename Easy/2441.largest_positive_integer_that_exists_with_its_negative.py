'''
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/?envType=daily-question&envId=2024-05-02
'''

from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg_set = set(num for num in nums if num < 0)

        ans = -float("inf")

        for num in nums:
            if num > 0 and -num in neg_set:
                ans = max(ans, num)

        return ans if ans != -float("inf") else -1
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findMaxK(nums = [-1, 2, -3, 3])
    assert test1 == 3
    
    test2 = sol.findMaxK(nums = [-1, 10, 6, 7, -7, 1])
    assert test2 == 7
    
    test3 = sol.findMaxK(nums = [-10, 8, 6, 7, -2, -3])
    assert test3 == -1
    