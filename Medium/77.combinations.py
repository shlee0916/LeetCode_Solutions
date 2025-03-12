'''
https://leetcode.com/problems/combinations/description/
'''

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, path, res, target_len):
            if len(path) > target_len:
                return
            elif len(path) == target_len:
                res.append(path)
                return

            for idx in range(len(nums)):
                dfs(nums[idx + 1:], path + [nums[idx]], res, target_len)

        result = []
        dfs(list(range(1, n + 1)), [], result, k)

        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.combine(n = 4, k = 2)
    print(test1, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    assert test1 == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    
    test2 = sol.combine(n = 1, k = 1)
    print(test2, [[1]])
    assert test2 == [[1]]
