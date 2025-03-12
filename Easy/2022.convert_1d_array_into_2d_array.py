'''
https://leetcode.com/problems/convert-1d-array-into-2d-array/?envType=daily-question&envId=2024-09-04
'''

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return [[]]

        new_array = [[0] * n for _ in range(m)]
        for idx, num in enumerate(original):
            new_array[idx // n][idx % n] = num

        return new_array


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.construct2DArray(original = [1, 2, 3, 4], m = 2, n = 2)
    assert test1 == [[1, 2], [3, 4]]
    
    test2 = sol.construct2DArray(original = [1, 2, 3], m = 1, n = 3)
    assert test2 == [[1, 2, 3]]

    test3 = sol.construct2DArray(original = [1, 2], m = 1, n = 1)
    assert test3 == [[]]
