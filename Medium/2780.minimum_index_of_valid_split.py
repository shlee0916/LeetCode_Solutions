'''
https://leetcode.com/problems/minimum-index-of-a-valid-split/?envType=daily-question&envId=2025-03-27
'''

from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        most_freq_num = nums[0]
        freq = 0
        for num in nums:
            if num == most_freq_num:
                freq += 1
            else:
                freq -= 1
            
            if freq == 0:
                most_freq_num = num
                freq = 1

        freq = 0
        for num in nums:
            if num == most_freq_num:
                freq += 1

        cnt = 0
        for idx, num in enumerate(nums):
            if num == most_freq_num:
                cnt += 1

            if cnt > (idx + 1) // 2 and (freq - cnt) > (len(nums) - idx - 1) // 2:
                return idx

        return -1


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumIndex(nums = [1, 2, 2, 2])
    assert test1 == 2

    test2 = sol.minimumIndex(nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1])
    assert test2 == 4

    test3 = sol.minimumIndex(nums = [3, 3, 3, 3, 7, 2, 2])
    assert test3 == -1
    