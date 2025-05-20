'''
https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
'''

from collections import Counter

from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = Counter()

        for idx in range(len(nums) - 1):
            if nums[idx] == key:
                cnt[nums[idx + 1]] += 1

        return cnt.most_common(1)[0][0]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.mostFrequent(nums = [1, 100, 200, 1, 100], key = 1)
    assert test1 == 100

    test2 = sol.mostFrequent(nums = [2, 2, 2, 2, 3], key = 2)
    assert test2 == 2
    