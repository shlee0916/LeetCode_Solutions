'''
https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/?envType=daily-question&envId=2023-11-19
'''

from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        ans = 0
        for idx, num in enumerate(nums[:-1], 1):
            if nums[idx] < num:
                ans += idx

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.reductionOperations(nums = [5, 1, 3])
    assert test1 == 3
    
    test2 = sol.reductionOperations(nums = [1, 1, 1])
    assert test2 == 0
    
    test3 = sol.reductionOperations(nums = [1, 1, 2, 2, 3])
    assert test3 == 4
    