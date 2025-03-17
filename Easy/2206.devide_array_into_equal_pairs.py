'''
https://leetcode.com/problems/divide-array-into-equal-pairs/?envType=daily-question&envId=2025-03-17
'''

from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_map = {}

        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

        return all(cnt % 2 == 0 for cnt in num_map.values())


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.divideArray(nums = [3, 2, 3, 2, 2, 2])
    assert test1 == True

    test2 = sol.divideArray(nums = [1, 2, 3, 4])
    assert test2 == False
    