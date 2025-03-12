'''
https://leetcode.com/problems/shifting-letters-ii/description/?envType=daily-question&envId=2025-01-05
'''

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        deltas = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            deltas[start] += (1 if direction == 1 else -1)
            if end + 1 < len(s):
                deltas[end + 1] -= (1 if direction == 1 else -1)

        cur_shift = 0
        new_letters = list(s)
        for idx in range(len(s)):
            cur_shift += deltas[idx]

            shifting = (cur_shift % 26 + 26) % 26
            new_letters[idx] = chr((ord(new_letters[idx]) - ord("a") + shifting) % 26 + ord("a"))
        
        return "".join(new_letters)
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.shiftingLetters(s = "abc", shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]])
    assert test1 == "ace"

    test2 = sol.shiftingLetters(s = "dztz", shifts = [[0, 0, 0], [1, 1, 1]])
    assert test2 == "catz"
    