'''
https://leetcode.com/problems/number-of-distinct-averages/
'''

from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        ans = set()

        nums.sort()
        for idx in range(len(nums) // 2):
            ans.add((nums[idx] + nums[-idx - 1]) / 2)
        
        return len(ans)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.distinctAverages(nums = [4, 1, 4, 0, 3, 5])
    assert test1 == 2

    test2 = sol.distinctAverages(nums = [1, 100])
    assert test2 == 1
    