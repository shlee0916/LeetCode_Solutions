'''
https://leetcode.com/problems/minesweeper/
'''

from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        row_limit = len(board)
        col_limit = len(board[0])

        search_dir = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
        stack = [click]
        while stack:
            cur_x, cur_y = stack.pop()
            mine_num = 0
            if board[cur_x][cur_y] == "E":
                next_search = []
                for delta_x, delta_y in search_dir:
                    new_x = cur_x + delta_x
                    new_y = cur_y + delta_y
                    
                    if 0 <= new_x < row_limit and 0 <= new_y < col_limit:
                        if board[new_x][new_y] == "M":
                            mine_num += 1

                        next_search.append((new_x, new_y))
                
                if mine_num > 0:
                    board[cur_x][cur_y] = str(mine_num)
                else:
                    board[cur_x][cur_y] = "B"
                    stack.extend(next_search[::-1])

        return board


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.updateBoard(board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]], click = [3, 0])
    assert test1 == [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
    
    test2 = sol.updateBoard(board = [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]], click = [1, 2])
    assert test2 == [["B", "1", "E", "1", "B"], ["B", "1", "X", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
    