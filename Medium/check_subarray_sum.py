'''
https://leetcode.com/problems/continuous-subarray-sum/
'''
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int):
        seen, cur = {0: -1}, 0
        for idx, num in enumerate(nums):
            cur = (cur + num) % abs(k) if k else cur + num

            if idx - seen.setdefault(cur, idx) > 1:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6), True)
    print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6), True)
    print(sol.checkSubarraySum([23, 2, 4, 6, 7], 13), False)
    print(sol.checkSubarraySum([0, 0], 1), True)