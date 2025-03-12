'''
https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
'''

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = 1
        cur_min = nums[0]
        cur_max = nums[0]
        for num in nums:
            cur_min = min(cur_min, num)
            cur_max = max(cur_max, num)

            if cur_max - cur_min > k:
                ans += 1
                cur_min = num
                cur_max = num

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.partitionArray(nums = [3, 6, 1, 2, 5], k = 2)
    assert test1 == 2

    test2 = sol.partitionArray(nums = [1, 2, 3], k = 1)
    assert test2 == 2

    test3 = sol.partitionArray(nums = [2, 2, 4, 5], k = 0)
    assert test3 == 3
    