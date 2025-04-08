'''
https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/?envType=daily-question&envId=2025-04-08
'''

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set()

        for idx, num in enumerate(nums[::-1]):
            if num in num_set:
                return (len(nums) - idx + 2) // 3

            num_set.add(num)

        return 0


if __name__  == "__main__":
    sol = Solution()

    test1 = sol.minimumOperations(nums = [1, 2, 3, 4, 2, 3, 3, 5, 7])
    assert test1 == 2

    test2 = sol.minimumOperations(nums = [4, 5, 6, 4, 4])
    assert test2 == 2

    test3 = sol.minimumOperations(nums = [6, 7, 8, 9])
    assert test3 == 0
    