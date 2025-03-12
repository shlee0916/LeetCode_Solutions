'''
https://leetcode.com/problems/binary-trees-with-factors/description/?envType=daily-question&envId=2023-10-26
'''

from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        dp = {num: 1 for num in arr}
        arr.sort()

        for idx, num in enumerate(arr):
            for mul_idx in range(idx):
                quot = arr[idx] // arr[mul_idx]
                if num % arr[mul_idx] == 0:
                    dp[num] += dp[arr[mul_idx]] * dp.get(quot, 0)
                    dp[num] %= mod

        return sum(dp.values()) % mod
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numFactoredBinaryTrees(arr = [2, 4])
    assert test1 == 3
    
    test2 = sol.numFactoredBinaryTrees(arr = [2, 4, 5, 10])
    assert test2 == 7
    