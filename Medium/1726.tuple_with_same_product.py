'''
https://leetcode.com/problems/tuple-with-same-product/?envType=daily-question&envId=2025-02-06
'''

from collections import defaultdict

from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        ans = 0
        for idx, num1 in enumerate(nums):
            for num2 in nums[idx + 1:]:
                product_map[num1 * num2] += 1

        for num, cand in product_map.items():
            if cand >= 2:
                ans += cand * (cand - 1) * 4
        
        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.tupleSameProduct(nums = [2, 3, 4, 6])
    assert test1 == 8

    test2 = sol.tupleSameProduct(nums = [1, 2, 4, 5, 10])
    assert test2 == 16
