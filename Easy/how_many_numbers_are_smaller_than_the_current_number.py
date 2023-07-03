'''
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
'''

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count = {}
        ans = []

        for idx, num in enumerate(sorted_nums):
            if num not in count:
                count[num] = idx

        for num in nums:
            ans.append(count[num])

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.smallerNumbersThanCurrent(nums = [8, 1, 2, 2, 3])
    assert test1 == [4, 0, 1, 1, 3]

    test2 = sol.smallerNumbersThanCurrent(nums = [6, 5, 4, 8])
    assert test2 == [2, 1, 0, 3]

    test3 = sol.smallerNumbersThanCurrent(nums = [7, 7, 7, 7])
    assert test3 == [0, 0, 0, 0]
    