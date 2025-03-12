'''
https://leetcode.com/problems/perfect-squares/description/
'''

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [0]

        for idx in range(1, n + 1):
            tmp_squares = []
            for iter_idx in range(1, int(idx ** 0.5) + 1):
                tmp_squares.append(squares[idx - iter_idx * iter_idx])

            squares.append(min(tmp_squares) + 1)

        return squares[n]
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numSquares(12)
    print(test1, 3)
    assert test1 == 3

    test2 = sol.numSquares(13)
    print(test2, 2)
    assert test2 == 2
