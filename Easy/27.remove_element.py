'''
https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans_idx = 0
        for num_idx in range(len(nums)):
            if nums[num_idx] != val:
                nums[ans_idx] = nums[num_idx]
                ans_idx += 1

        return ans_idx


if __name__ == "__main__":
    sol = Solution()

    test1_nums = [3, 2, 2, 3]
    test1_ans = [2, 2]
    test1 = sol.removeElement(nums = test1_nums, val = 3)
    assert test1 == 2
    assert all(test1_ans[idx] == test1_nums[idx] for idx in range(test1))

    test2_nums = [0, 1, 2, 2, 3, 0, 4, 2]
    test2_ans = [0, 1, 3, 0, 4]
    test2 = sol.removeElement(nums = test2_nums, val = 2)
    assert test2 == 5
    assert all(test2_ans[idx] == test2_nums[idx] for idx in range(test2))
