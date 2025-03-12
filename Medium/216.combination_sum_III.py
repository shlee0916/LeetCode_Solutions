'''
https://leetcode.com/problems/combination-sum-iii/description/
'''

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(nums, limit_len, target, path, result):
            if target < 0 or limit_len < 0:
                return

            if target == 0 and limit_len == 0:
                result.append(path)

            for idx in range(len(nums)):
                dfs(nums[idx + 1:], limit_len - 1, target - nums[idx], path + [nums[idx]], result)

        result = []
        dfs(range(1, 10), k, n, [], result)
        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.combinationSum3(k = 3, n = 7)
    print(test1, [[1, 2, 4]])
    assert test1 == [[1, 2, 4]]
    
    test2 = sol.combinationSum3(k = 3, n = 9)
    print(test2, [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
    assert test2 == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    
    test3 = sol.combinationSum3(k = 4, n = 1)
    print(test3, [])
    assert test3 == []
    