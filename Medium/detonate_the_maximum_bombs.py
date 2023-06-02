'''
https://leetcode.com/problems/detonate-the-maximum-bombs/description/
'''

from math import sqrt
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        num_bomb = len(bombs)
        in_range = {idx: [] for idx in range(num_bomb)}

        for blow_idx, (blow_x, blow_y, redius) in enumerate(bombs):
            for idx, (x, y, _) in enumerate(bombs):
                distance = sqrt((blow_x - x) ** 2 + (blow_y - y) ** 2)
                if blow_idx != idx:
                    if distance <= redius:
                        in_range[blow_idx].append(idx)

        max_chain = 0
        for idx in range(num_bomb):
            cur_chain = 0
            stack = [idx]
            already_blowed_up = set([idx])
            while stack:
                cur_bomb = stack.pop()
                cur_chain += 1

                next_bombs = in_range[cur_bomb]
                for bomb in next_bombs:
                    if bomb not in already_blowed_up:
                        stack.append(bomb)
                        already_blowed_up.add(bomb)

            max_chain = max(max_chain, cur_chain)

        return max_chain


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumDetonation(bombs = [[2, 1, 3], [6, 1, 4]])
    assert test1 == 2

    test2 = sol.maximumDetonation(bombs = [[1, 1, 5], [10, 10, 5]])
    assert test2 == 1

    test3 = sol.maximumDetonation(bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]])
    assert test3 == 5
    