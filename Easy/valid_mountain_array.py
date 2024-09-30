'''
https://leetcode.com/problems/valid-mountain-array/
'''

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        left = 0
        right = length - 1

        while left + 1 < length and arr[left] < arr[left + 1]:
            left += 1
        
        while right > 0 and arr[right - 1] > arr[right]:
            right -= 1

        return 0 < left == right < length - 1
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.validMountainArray(arr = [2, 1])
    assert test1 == False

    test2 = sol.validMountainArray(arr = [3, 5, 5])
    assert test2 == False

    test3 = sol.validMountainArray(arr = [0, 3, 2, 1])
    assert test3 == True
