'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        left = 2
        right = 2
        
        while right < len(nums):
            if nums[left - 2] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left


if __name__ == "__main__":
    sol = Solution()

    test1_list = [1, 1, 1, 2, 2, 3]
    test1 = sol.removeDuplicates(nums = test1_list)
    test1_ans = [1, 1, 2, 2, 3]
    assert test1 == 5
    assert all(test1_list[idx] == test1_ans[idx] for idx in range(test1))

    test2_list = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    test2 = sol.removeDuplicates(nums = test2_list)
    test2_ans = nums = [0, 0, 1, 1, 2, 3, 3]
    assert test2 == 7
    assert all(test2_list[idx] == test2_ans[idx] for idx in range(test2))
