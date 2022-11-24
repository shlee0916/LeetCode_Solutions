'''
https://leetcode.com/problems/word-search/description/
'''
from typing import List
from itertools import product


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ### -------------------------------------------------- ###
        def dfs(w_idx, r_idx, c_idx):
            if self.found:
                return

            if len(word) == w_idx:
                self.found = True
                return

            if r_idx < 0 or r_idx >= h_size or c_idx < 0 or c_idx >= v_size :
                return

            ch = board[r_idx][c_idx]
            if ch != word[w_idx]:
                return

            board[r_idx][c_idx] = "#"
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(w_idx + 1, r_idx + x, c_idx + y)
            board[r_idx][c_idx] = ch
        ### -------------------------------------------------- ###

        self.found = False
        h_size, v_size = len(board), len(board[0])

        for r_idx, c_idx in product(range(h_size), range(v_size)):
            if self.found:
                return True
            dfs(0, r_idx, c_idx)

        return self.found
    

if __name__ == "__main__":
    sol = Solution()

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

    test1 = sol.exist(board, "ABCCED")
    print(test1, True)
    assert test1 == True

    test2 = sol.exist(board, "SEE")
    print(test2, True)
    assert test2 == True

    test3 = sol.exist(board, "ABCB")
    print(test3, False)
    assert test3 == False
