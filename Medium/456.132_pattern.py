'''
https://leetcode.com/problems/132-pattern/description/?envType=daily-question&envId=2023-09-30
'''

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float("-inf")

        for num in nums[::-1]:
            if num < third:
                return True

            while stack and stack[-1] < num:
                third = stack.pop()

            stack.append(num)

        return False
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.find132pattern(nums = [1, 2, 3, 4])
    assert test1 == False
    
    test2 = sol.find132pattern(nums = [3, 1, 4, 2])
    assert test2 == True
    
    test3 = sol.find132pattern(nums = [-1, 3, 2, 0])
    assert test3 == True
    