'''
https://leetcode.com/problems/where-will-the-ball-fall/
'''
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        start = [idx for idx in range(len(grid[0]))]
        
        box_len = len(start)
        
        for r_idx, slips in enumerate(grid):
            for b_idx, (slip, ball) in enumerate(zip(slips, start)):
                if ball != -1:
                    next_pos = slips[ball] + ball
                    
                    if next_pos < 0:
                        next_pos = -1
                    elif next_pos >= box_len:
                        next_pos = -1
                    elif slips[ball] == 1 and ball < box_len - 1 and slips[ball + 1] == -1:
                        next_pos = -1
                    elif slips[ball] == -1 and ball > 1 and slips[ball - 1] == 1:
                        next_pos = -1
                        
                    start[b_idx] = next_pos
                
        return start
        
        
if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]])
    print(test1,  [1, -1, -1, -1, -1])
    assert test1 == [1, -1, -1, -1, -1]

    test2 = sol.findBall([[-1]])
    print(test2, [-1])
    assert test2 == [-1]

    test3 = sol.findBall([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]])
    print(test3, [0, 1, 2, 3, 4, -1])
    assert test3 == [0, 1, 2, 3, 4, -1]