'''
https://leetcode.com/problems/find-the-winner-of-an-array-game/description/?envType=daily-question&envId=2023-11-08
'''

from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_cnt = 0
        winner = arr[0]
        for num in arr[1:]:
            if num > winner:
                winner = num
                win_cnt = 0

            win_cnt += 1
            
            if win_cnt == k:
                break

        return winner
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getWinner(arr = [2, 1, 3, 5, 4, 6, 7], k = 2)
    assert test1 == 5

    test2 = sol.getWinner(arr = [3, 2, 1], k = 10)
    assert test2 == 3
    