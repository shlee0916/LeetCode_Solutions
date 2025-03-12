'''
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
'''

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1

        return res


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findDuplicates(nums = [4, 3, 2, 7, 8, 2, 3, 1])
    print(test1, [2, 3])
    assert test1 == [2, 3]

    test2 = sol.findDuplicates(nums = [1, 1, 2])
    print(test2, [1])
    assert test2 == [1]
    
    test3 = sol.findDuplicates(nums = [1])
    print(test3, [])
    assert test3 == []
    