'''
https://leetcode.com/problems/largest-perimeter-triangle/
'''
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_num = sorted(nums)[::-1]
        
        for idx in range(len(sorted_num) - 2):
            if sorted_num[idx] < sorted_num[idx + 1] + sorted_num[idx + 2]:
                return sorted_num[idx] + sorted_num[idx + 1] + sorted_num[idx + 2]
                
        return 0


if __name__ == "__main__":
    sol = Solution()

    print(sol.largestPerimeter([2, 1, 2]), 5)
    print(sol.largestPerimeter([1, 2, 1]), 0)