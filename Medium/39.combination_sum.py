'''
https://leetcode.com/problems/combination-sum/description/
'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for idx in range(len(nums)):
                dfs(nums[idx:], target - nums[idx], path + [nums[idx]], res)

        res = []
        dfs(candidates, target, [], res)

        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.combinationSum(candidates = [2, 3, 6, 7], target = 7)
    print(test1, [[2, 2, 3], [7]])
    assert test1 == [[2, 2, 3], [7]]
    
    test2 = sol.combinationSum(candidates = [2, 3, 5], target = 8)
    print(test2, [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    assert test2 == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    
    test3 = sol.combinationSum(candidates = [2], target = 1)
    print(test3, [])
    assert test3 == []
    