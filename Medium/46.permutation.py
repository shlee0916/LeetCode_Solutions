'''
https://leetcode.com/problems/permutations/
'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def switch(s_idx, e_idx, nums):
            new_nums = list(nums)
            new_nums[s_idx], new_nums[e_idx] = new_nums[e_idx], new_nums[s_idx]
            return new_nums
        
        result = [nums]
        for s_idx in range(len(nums) - 1):
            for res in result[:]:
                for e_idx in range(s_idx + 1, len(nums)):
                    result.append(switch(s_idx, e_idx, res))
                    
        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.permute([1, 2, 3]))