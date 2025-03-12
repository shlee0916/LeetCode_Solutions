'''
https://leetcode.com/problems/subarray-sum-equals-k/description/
'''

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sums = 0
        sums_table = {}
        sums_table[0] = 1

        for idx in range(len(nums)):
            sums += nums[idx]
            ans += sums_table.get(sums - k, 0)
            sums_table[sums] = sums_table.get(sums, 0) + 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.subarraySum(nums = [1, 1, 1], k = 2)
    assert test1 == 2
    
    test2 = sol.subarraySum(nums = [1, 2, 3], k = 3)
    assert test2 == 2
    