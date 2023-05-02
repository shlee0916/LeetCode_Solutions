'''
https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
'''

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_count = 0

        for num in nums:
            if num == 0:
                return 0
            
            if num < 0:
                neg_count += 1

        return 1 if neg_count % 2 == 0 else -1


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.arraySign(nums = [-1, -2, -3, -4, 3, 2, 1])
    assert test1 == 1

    test2 = sol.arraySign(nums = [1, 5, 0, 2, -3])
    assert test2 == 0

    test3 = sol.arraySign(nums = [-1, 1, -1, 1, -1])
    assert test3 == -1
    