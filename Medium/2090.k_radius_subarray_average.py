'''
https://leetcode.com/problems/k-radius-subarray-averages/description/
'''

from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)

        left = 0
        diameter = 2 * k + 1
        cur_sum = 0
        for right, num in enumerate(nums):
            cur_sum += num

            if (right - left + 1) >= diameter:
                ans[left + k] = cur_sum // diameter
                cur_sum -= nums[left]
                left += 1

        return ans
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.getAverages(nums = [7, 4, 3, 9, 1, 8, 5, 2, 6], k = 3)
    assert test1 == [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    
    test2 = sol.getAverages(nums = [100000], k = 0)
    assert test2 == [100000]

    test3 = sol.getAverages(nums = [8], k = 100000)
    assert test3 == [-1]
    