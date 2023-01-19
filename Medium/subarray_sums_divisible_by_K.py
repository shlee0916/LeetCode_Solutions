'''
https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
'''

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        count = [1] + [0] * k

        for num in nums:
            prefix = (prefix + num) % k
            res += count[prefix]
            count[prefix] += 1

        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.subarraysDivByK(nums = [4, 5, 0, -2, -3, 1], k = 5)
    print(test1, 7)
    assert test1 == 7

    test2 = sol.subarraysDivByK(nums = [5], k = 9)
    print(test2, 0)
    assert test2 == 0
