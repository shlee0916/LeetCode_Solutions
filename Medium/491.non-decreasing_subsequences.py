'''
https://leetcode.com/problems/non-decreasing-subsequences/description/
'''

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs = {()}
        for num in nums:
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}

        return [list(sub) for sub in subs if len(sub) >= 2]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findSubsequences(nums = [4, 6, 7, 7])
    print(test1, [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]])
    assert sorted(test1) == sorted([[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]])

    test2 = sol.findSubsequences(nums = [4, 4, 3, 2, 1])
    print(test2, [[4, 4]])
    assert test2 == [[4, 4]]
