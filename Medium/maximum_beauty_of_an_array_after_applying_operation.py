'''
https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/?envType=daily-question&envId=2024-12-11
'''

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        sorted_num = sorted(nums)

        ans = 1
        left = 0
        for right in range(len(nums)):
            if sorted_num[right] - sorted_num[left] > 2 * k:
                left += 1
            else:
                ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumBeauty(nums = [4, 6, 1, 2], k = 2)
    assert test1 == 3

    test2 = sol.maximumBeauty(nums = [1, 1, 1, 1], k = 10)
    assert test2 == 4
    