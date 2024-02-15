'''
https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/?envType=daily-question&envId=2024-02-15
'''

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        cur_perimeter = sum(nums)

        for num in nums[::-1]:
            cur_perimeter -= num
            if cur_perimeter > num:
                return cur_perimeter + num

        return -1


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.largestPerimeter(nums = [5, 5, 5])
    assert test1 == 15

    test2 = sol.largestPerimeter(nums = [1, 12, 1, 2, 5, 50, 3])
    assert test2 == 12

    test3 = sol.largestPerimeter(nums = [5, 5, 50])
    assert test3 == -1
    