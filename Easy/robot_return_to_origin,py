'''
https://leetcode.com/problems/robot-return-to-origin/description/
'''

from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ch_cnt = Counter(moves)

        return ch_cnt["U"] == ch_cnt["D"] and ch_cnt["L"] == ch_cnt["R"]
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.judgeCircle(moves = "UD")
    assert test1 == True
    
    test2 = sol.judgeCircle(moves = "LL")
    assert test2 == False
    