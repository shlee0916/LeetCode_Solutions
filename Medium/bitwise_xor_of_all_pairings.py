'''
https://leetcode.com/problems/bitwise-xor-of-all-pairings/?envType=daily-question&envId=2025-01-16
'''

from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num1_xor = 0
        num2_xor = 0

        for num in nums1:
            num1_xor ^= num
        
        for num in nums2:
            num2_xor ^= num

        return (len(nums2) % 2 * num1_xor) ^ (len(nums1) % 2 * num2_xor)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.xorAllNums(nums1 = [2, 1, 3], nums2 = [10, 2, 5, 0])
    assert test1 == 13

    test2 = sol.xorAllNums(nums1 = [1, 2], nums2 = [3, 4])
    assert test2 == 0
    