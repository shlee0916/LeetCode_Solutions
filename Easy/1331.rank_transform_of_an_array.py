'''
https://leetcode.com/problems/rank-transform-of-an-array/?envType=daily-question&envId=2024-10-02
'''

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {num: rank for rank, num in enumerate(sorted(list(set(arr))))}

        return [rank[num] + 1 for num in arr]
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.arrayRankTransform(arr = [40, 10, 20, 30])
    assert test1 == [4, 1, 2, 3]

    test2 = sol.arrayRankTransform(arr = [100, 100, 100])
    assert test2 == [1, 1, 1]

    test3 = sol.arrayRankTransform(arr = [37, 12, 28, 9, 100, 56, 80, 5, 12])
    assert test3 == [5, 3, 4, 2, 8, 6, 7, 1, 3]