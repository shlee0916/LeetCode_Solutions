'''
https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description/?envType=daily-question&envId=2025-05-23
'''

from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = 0
        cnt = 0
        min_change = float("inf")

        for num in nums:
            ans += max(num ^ k, num)
            cnt += num ^ k > num

            min_change = min(min_change, abs(num - (num ^ k)))

        return ans - min_change if cnt % 2 == 1 else ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumValueSum(nums = [1, 2, 1], k = 3, edges = [[0, 1], [0, 2]])
    assert test1 == 6

    test2 = sol.maximumValueSum(nums = [2, 3], k = 7, edges = [[0, 1]])
    assert test2 == 9

    test3 = sol.maximumValueSum(nums = [7, 7, 7, 7, 7, 7], k = 3, edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]])
    assert test3 == 42
    