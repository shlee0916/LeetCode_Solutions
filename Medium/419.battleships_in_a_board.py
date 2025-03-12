'''
https://leetcode.com/problems/battleships-in-a-board/description/
'''

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                if (board[row_idx][col_idx] == "X" and
                    (row_idx == 0 or board[row_idx - 1][col_idx] == ".") and
                    (col_idx == 0 or board[row_idx][col_idx - 1] == ".")):
                    ans += 1
                    
        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countBattleships(board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]])
    assert test1 == 2
    
    test2 = sol.countBattleships(board = [["."]])
    assert test2 == 0
    