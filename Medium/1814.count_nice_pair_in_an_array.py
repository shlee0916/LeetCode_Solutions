'''
https://leetcode.com/problems/count-nice-pairs-in-an-array/description/?envType=daily-question&envId=2023-11-21
'''

from collections import Counter

from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()

        for num in nums:
            rev_num = int(str(num)[::-1])
            ans += cnt[num - rev_num]
            cnt[num - rev_num] += 1

        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countNicePairs(nums = [42, 11, 1, 97])
    assert test1 == 2

    test2 = sol.countNicePairs(nums = [13, 10, 35, 24, 76])
    assert test2 == 4
    