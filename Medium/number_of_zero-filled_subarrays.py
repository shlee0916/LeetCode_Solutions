'''
https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
'''

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        cur_sub = 0
        for num in nums:
            if num == 0:
                cur_sub += 1
                total += cur_sub
            else:
                cur_sub = 0

        return total
            

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.zeroFilledSubarray(nums = [1, 3, 0, 0, 2, 0, 0, 4])
    print(test1, 6)
    assert test1 == 6
    
    test2 = sol.zeroFilledSubarray(nums = [0, 0, 0, 2, 0, 0])
    print(test2, 9)
    assert test2 == 9

    test3 = sol.zeroFilledSubarray(nums = [2, 10, 2019])
    print(test3, 0)
    assert test3 == 0
    