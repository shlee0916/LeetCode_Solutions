'''
https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
'''

from collections import Counter

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        nums_cnt = Counter(nums)

        for num in nums_cnt:
            cnt += min(nums_cnt[num], nums_cnt[k - num])

        return cnt // 2


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxOperations(nums = [1, 2, 3, 4], k = 5)
    assert test1 == 2

    test2 = sol.maxOperations(nums = [3, 1, 3, 4, 3], k = 6)
    assert test2 == 1
    