'''
https://leetcode.com/problems/maximum-distance-in-arrays/?envType=daily-question&envId=2024-08-16
'''

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]
        ans = 0

        for arr in arrays[1:]:
            ans = max(ans, abs(cur_min - arr[-1]), abs(cur_max - arr[0]))
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxDistance(arrays = [[1, 2, 3], [4, 5], [1, 2, 3]])
    assert test1 == 4
    
    test2 = sol.maxDistance(arrays = [[1], [1]])
    assert test2 == 0
    