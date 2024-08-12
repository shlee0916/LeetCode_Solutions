'''
https://leetcode.com/problems/contiguous-array/?envType=daily-question&envId=2024-08-04
'''

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        num_map = {0: -1}
        ans = 0

        for idx, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in num_map:
                ans = max(ans, idx - num_map[count])
            else:
                num_map[count] = idx

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findMaxLength(nums = [0, 1])
    assert test1 == 2

    test2 = sol.findMaxLength(nums = [0, 1, 0])
    assert test2 == 2
    