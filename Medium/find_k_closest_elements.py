'''
https://leetcode.com/problems/find-k-closest-elements/
'''
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]


if __name__ == "__main__":
    sol = Solution()

    print(sol.findClosestElements(arr = [1, 2, 3, 4, 5], k = 4, x = 3), [1, 2, 3, 4])
    print(sol.findClosestElements(arr = [1, 2, 3, 4, 5], k = 4, x = -1), [1, 2, 3, 4])