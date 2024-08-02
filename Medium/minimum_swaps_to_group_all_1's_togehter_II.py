'''
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/?envType=daily-question&envId=2024-08-02
'''

from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        win_size = nums.count(1)
        expanded_arr = nums * 2

        ans = win_size
        cur_zeros = expanded_arr[:win_size].count(0)

        for idx in range(win_size, len(expanded_arr)):
            if expanded_arr[idx - win_size] == 0:
                cur_zeros -= 1
            if expanded_arr[idx] == 0:
                cur_zeros += 1
                
            ans = min(ans, cur_zeros)

        return ans
            


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minSwaps(nums = [0, 1, 0, 1, 1, 0, 0])
    assert test1 == 1

    test2 = sol.minSwaps(nums = [0, 1, 1, 1, 0, 0, 1, 1, 0])
    assert test2 == 2

    test3 = sol.minSwaps(nums = [1, 1, 0, 0, 1])
    assert test3 == 0
    