'''
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
'''

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.peakIndexInMountainArray(arr = [0, 1, 0]) 
    assert test1 == 1
    
    test2 = sol.peakIndexInMountainArray(arr = [0, 2, 1, 0])
    assert test2 == 1
    
    test3 = sol.peakIndexInMountainArray(arr = [0, 10, 5, 2])
    assert test3 == 1
    