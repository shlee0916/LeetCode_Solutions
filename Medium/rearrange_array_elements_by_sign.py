'''
https://leetcode.com/problems/rearrange-array-elements-by-sign/?envType=daily-question&envId=2024-02-14
'''

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        pos_idx = 0
        neg_idx = 1

        for num in nums:
            if num > 0:
                ans[pos_idx] = num
                pos_idx += 2
            else:
                ans[neg_idx] = num
                neg_idx += 2

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.rearrangeArray(nums = [3, 1, -2, -5, 2, -4])
    assert test1 == [3, -2, 1, -5, 2, -4]

    test2 = sol.rearrangeArray(nums = [-1, 1])
    assert test2 == [1, -1]

    test3 = sol.rearrangeArray(nums = [28, -41, 22, -8, -37, 46, 35, -9, 18, -6, 19, -26, -37, -10, -9, 15, 14, 31])
    assert test3 == [28, -41, 22, -8, 46, -37, 35, -9, 18, -6, 19, -26, 15, -37, 14, -10, 31, -9]
    