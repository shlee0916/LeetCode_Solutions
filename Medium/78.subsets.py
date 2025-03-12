'''
https://leetcode.com/problems/subsets/description/
'''

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            res.append(path)
            for idx in range(len(nums)):
                dfs(nums[idx + 1:], path + [nums[idx]], res)
        
        res = []
        dfs(nums, [], res)
        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.subsets(nums = [1, 2, 3])
    print(test1, [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert sorted(test1) == sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    test2 = sol.subsets(nums = [0])
    print(test2, [[], [0]])
    assert test2 == [[], [0]]
