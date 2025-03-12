'''
https://leetcode.com/problems/sort-an-array/description/
'''

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        merged = []
        low = high = 0
        while low < len(left) and high < len(right):
            if left[low] < right[high]:
                merged.append(left[low])
                low += 1
            else:
                merged.append(right[high])
                high += 1

        merged += left[low:]
        merged += right[high:]

        return merged
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.sortArray([5, 2, 3, 1])
    print(test1, [1, 2, 3, 5])
    assert test1 == [1, 2, 3, 5]

    test2 = sol.sortArray([5, 1, 1, 2, 0, 0])
    print(test2, [0, 0, 1, 1, 2, 5])
    assert test2 == [0, 0, 1, 1, 2, 5]
    