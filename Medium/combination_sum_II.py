'''
https://leetcode.com/problems/combination-sum-ii/description/
'''

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, idx, path, target, res):
            if target < 0:
                return

            if target == 0:
                res.append(path)
                return

            for cur_idx in range(idx, len(nums)):
                if cur_idx > idx and nums[cur_idx] == nums[cur_idx - 1]:
                    continue

                dfs(nums, cur_idx + 1, path + [nums[cur_idx]], target - nums[cur_idx], res)

        result = []
        dfs(sorted(candidates), 0, [], target, result)

        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.combinationSum2(candidates = [10, 1, 2, 7, 6, 1, 5], target = 8)
    print(test1, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    assert test1 == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    
    test2 = sol.combinationSum2(candidates = [2, 5, 2, 1, 2], target = 5)
    print(test2, [[1, 2, 2], [5]])
    assert test2 == [[1, 2, 2], [5]]
    