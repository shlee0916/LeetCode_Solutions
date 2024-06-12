'''
https://leetcode.com/problems/max-consecutive-ones/
'''

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur = 0

        for num in nums:
            if num == 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findMaxConsecutiveOnes(nums = [1, 1, 0, 1, 1, 1])
    assert test1 == 3
    
    test2 = sol.findMaxConsecutiveOnes(nums = [1, 0, 1, 1, 0, 1])
    assert test2 == 2
    