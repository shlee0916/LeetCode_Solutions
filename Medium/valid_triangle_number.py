'''
https://leetcode.com/problems/valid-triangle-number/description/
'''

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        
        for third in range(2, len(nums)):
            first = 0
            second = third - 1

            while first < second:
                if nums[first] + nums[second] > nums[third]:
                    ans += second - first
                    second -= 1
                else:
                    first += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.triangleNumber(nums = [2, 2, 3, 4])
    assert test1 == 3

    test2 = sol.triangleNumber(nums = [4, 2, 3, 4])
    assert test2 == 4
    