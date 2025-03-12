'''
https://leetcode.com/problems/kth-missing-positive-number/description/
'''

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = [num for num in range(len(arr) + k + 1) if num not in arr]
        return nums[k]


# Binary search
class BSolution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid

        return right + k
    

if __name__ == "__main__":
    sol = Solution()
    bsol = BSolution()

    test1 = sol.findKthPositive(arr = [2, 3, 4, 7, 11], k = 5)
    print(test1, 9)
    assert test1 == 9

    test1 = bsol.findKthPositive(arr = [2, 3, 4, 7, 11], k = 5)
    assert test1 == 9

    test2 = sol.findKthPositive(arr = [1, 2, 3, 4], k = 2)
    print(test2, 6)
    assert test2 == 6

    test2 = bsol.findKthPositive(arr = [1, 2, 3, 4], k = 2)
    assert test2 == 6
    