'''
https://leetcode.com/problems/triangle/
'''
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r_idx, row in enumerate(triangle[1:]):
            for idx, num in enumerate(row):
                if idx == 0:
                    triangle[r_idx + 1][idx] = num + triangle[r_idx][idx]
                elif idx == r_idx + 1:
                    triangle[r_idx + 1][idx] = num + triangle[r_idx][idx - 1]
                else:
                    triangle[r_idx + 1][idx] = min(num + triangle[r_idx][idx], num + triangle[r_idx][idx - 1])
                
        
        return min(triangle[-1])


if __name__ == "__main__":
    sol = Solution()

    print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11)
    print(sol.minimumTotal([[-10]]), -10)