'''
https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
'''

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans += min(num % 3, 3 - (num % 3))

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minimumOperations(nums = [1, 2, 3, 4])
    assert test1 == 3
    
    test2 = sol.minimumOperations(nums = [3, 6, 9])
    assert test2 == 0
    