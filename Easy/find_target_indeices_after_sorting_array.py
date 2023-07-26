'''
https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
'''

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = 0

        for num in nums:
            if num < target:
                left_index += 1
            if num == target:
                right_index += 1

        return list(range(left_index, left_index + right_index))
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.targetIndices(nums = [1, 2, 5, 2, 3], target = 2)
    assert test1 == [1, 2]
    
    test2 = sol.targetIndices(nums = [1, 2, 5, 2, 3], target = 3)
    assert test2 == [3]
    
    test3 = sol.targetIndices(nums = [1, 2, 5, 2, 3], target = 5)
    assert test3 == [4]
    