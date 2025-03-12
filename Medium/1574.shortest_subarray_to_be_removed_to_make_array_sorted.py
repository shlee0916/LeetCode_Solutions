'''
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/?envType=daily-question&envId=2024-11-15
'''

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right and arr[left + 1] >= arr[left]:
            left += 1
        
        if left == len(arr) - 1:
            return 0 ## already sorted arr

        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        ans = min(len(arr) - left - 1, right)

        for idx in range(left + 1):
            if arr[idx] <= arr[right]:
                ans = min(ans, right - idx - 1)

            elif right < len(arr) - 1:
                right += 1

            else:
                break

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findLengthOfShortestSubarray(arr = [1, 2, 3, 10, 4, 2, 3, 5])
    assert test1 == 3

    test2 = sol.findLengthOfShortestSubarray(arr = [5, 4, 3, 2, 1])
    assert test2 == 4

    test3 = sol.findLengthOfShortestSubarray(arr = [1, 2, 3])
    assert test3 == 0
    