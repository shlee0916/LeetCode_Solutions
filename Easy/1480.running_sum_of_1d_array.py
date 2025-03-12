'''
https://leetcode.com/problems/running-sum-of-1d-array/description/
'''

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for num in nums[1:]:
            ans.append(ans[-1] + num)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.runningSum(nums = [1, 2, 3, 4])
    assert test1 == [1, 3, 6, 10]
    
    test2 = sol.runningSum(nums = [1, 1, 1, 1, 1])
    assert test2 == [1, 2, 3, 4, 5]
    
    test3 = sol.runningSum(nums = [3,1,2,10,1])
    assert test3 == [3, 4, 6, 16, 17]
    