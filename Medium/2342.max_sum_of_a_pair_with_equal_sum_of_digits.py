'''
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/?envType=daily-question&envId=2025-02-12
'''

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        nums_map = {}
        for num in nums:
            digit_sum = sum(int(ch) for ch in str(num))
            
            if digit_sum not in nums_map:
                nums_map[digit_sum] = num
            else:
                ans = max(ans, num + nums_map[digit_sum])
                nums_map[digit_sum] = max(num, nums_map[digit_sum])

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumSum(nums = [18, 43, 36, 13, 7])
    assert test1 == 54

    test2 = sol.maximumSum(nums = [10, 12, 19, 14])
    assert test2 == -1
    