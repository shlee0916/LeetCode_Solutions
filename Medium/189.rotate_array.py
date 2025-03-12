'''
https://leetcode.com/problems/rotate-array/description/
'''

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        rotate_num = k % length

        for _ in range(length - rotate_num):
            num = nums.pop(0)
            nums.append(num)
            

if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums, k = 3)
    print(nums, [5, 6, 7, 1, 2, 3, 4])
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    sol.rotate(nums, k = 2)
    print(nums, [3, 99, -1, -100])
    assert nums == [3, 99, -1, -100]
