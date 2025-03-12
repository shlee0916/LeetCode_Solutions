'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_idx = 1

        for idx in range(len(nums) - 1):
            if nums[idx] != nums[idx + 1]:
                nums[nums_idx] = nums[idx + 1]
                nums_idx += 1

        return nums_idx


if __name__ == "__main__":
    sol = Solution()

    test1_list = [1, 1, 2]
    test1_sol = [1, 2]
    test1 = sol.removeDuplicates(test1_list)
    for idx in range(test1):
        assert test1_list[idx] == test1_sol[idx]
    print(test1_list, test1_sol)

    test2_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    test2_sol = [0, 1, 2, 3, 4]
    test2 = sol.removeDuplicates(test2_list)
    for idx in range(test2):
        assert test2_list[idx] == test2_sol[idx]
    print(test2_list, test2_sol)