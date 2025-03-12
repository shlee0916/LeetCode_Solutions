'''
https://leetcode.com/problems/house-robber-ii/description/
'''
from typing import List


class Solution:
    def _rob(self, nums: List[int]) -> int:
        rob_a, rob_b = 0, 0
        for num in nums:
            rob_a, rob_b = rob_b, max(rob_a + num, rob_b)
            
        return rob_b

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(self._rob(nums[1:]), self._rob(nums[:-1]))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.rob([2,3,2])
    print(test1, 3)
    assert test1 == 3

    test2 = sol.rob([1,2,3,1])
    print(test2, 4)
    assert test2 == 4

    test3 = sol.rob([1,2,3])
    print(test3, 3)
    assert test3 == 3
