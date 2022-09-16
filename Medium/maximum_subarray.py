'''
https://leetcode.com/problems/maximum-subarray/
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -100000
        sums = 0
        
        for num in nums:
            sums += num
            ans = max(sums, ans)
            
            if sums < 0:
                sums = 0
            
        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)