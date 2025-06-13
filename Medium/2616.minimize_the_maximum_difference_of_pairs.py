'''
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/?envType=daily-question&envId=2025-06-13
'''

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        length = len(nums)
        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            num_pair = 0
            idx = 1
            while idx < length:
                if nums[idx] - nums[idx - 1] <= mid:
                    num_pair += 1
                    idx += 1
                idx += 1

            if num_pair >= p:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimizeMax(nums = [10, 1, 2, 7, 1, 3], p = 2)
    assert test1 == 1

    test2 = sol.minimizeMax(nums = [4, 2, 1, 2], p = 1)
    assert test2 == 0
