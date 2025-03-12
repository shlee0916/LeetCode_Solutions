'''
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
'''
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        num_arrow, arrow_idx = 0, 0
        points.sort(key = lambda p: p[1])
        
        for start, end in points:
            if num_arrow == 0 or arrow_idx < start:
                num_arrow += 1
                arrow_idx = end
                    
        return num_arrow



if __name__ == "__main__":
    sol = Solution()

    print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]), 2)
    print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]), 4)
    print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]), 2)