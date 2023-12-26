'''
https://leetcode.com/problems/relative-sort-array/description/
'''

from collections import Counter

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_cnt = Counter(arr1)

        ans = []
        for num in arr2:
            ans.extend([num] * arr1_cnt[num])
            arr1_cnt.pop(num)

        rest_nums = []
        for key, value in arr1_cnt.items():
            rest_nums.extend([key] * value)

        return ans + sorted(rest_nums)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.relativeSortArray(arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2 = [2, 1, 4, 3, 9, 6])
    assert test1 == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    
    test2 = sol.relativeSortArray(arr1 = [28, 6, 22, 8, 44, 17], arr2 = [22, 28, 8, 6])
    assert test2 == [22, 28, 8, 6, 17, 44]
    