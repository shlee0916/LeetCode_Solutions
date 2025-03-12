'''
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/?envType=daily-question&envId=2023-12-11
'''

from collections import Counter

from typing import List


class Solution:
    # def findSpecialInteger(self, arr: List[int]) -> int:
    #     num_cnt = Counter(arr)

    #     limit = len(arr) / 4
    #     for num, cnt in num_cnt.items():
    #         if cnt > limit:
    #             ans = num

    #     return ans

    
    # Binary search
    def findSpecialInteger(self, arr: List[int]) -> int:
        def binary_search(target: int, arr: List[int]) -> int:
            left = 0
            right = len(arr) - 1

            while left < right:
                mid = (left + right) // 2

                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            return left
        
        target_len = len(arr) // 4
        for num in set(arr):
            first_idx = binary_search(num, arr)

            if first_idx + target_len < len(arr) and arr[first_idx] == arr[first_idx + target_len]:
                return arr[first_idx]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findSpecialInteger(arr = [1, 2, 2, 6, 6, 6, 6, 7, 10])
    assert test1 == 6

    test2 = sol.findSpecialInteger(arr = [1, 1])
    assert test2 == 1

    test3 = sol.findSpecialInteger(arr = [5668, 5668, 5668, 5668, 22011])
    assert test3 == 5668

    test4 = sol.findSpecialInteger(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 12])
    assert test4 == 12
