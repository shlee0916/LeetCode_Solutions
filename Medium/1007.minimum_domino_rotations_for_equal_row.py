'''
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/?envType=daily-question&envId=2025-05-03
'''

from collections import Counter

from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_target = Counter(tops).most_common(1)[0]
        bot_target = Counter(bottoms).most_common(1)[0]

        for idx, (top_ele, bot_ele) in enumerate(zip(tops, bottoms)):
            if top_ele != top_target[0] and bot_ele == top_target[0]:
                tops[idx]  = top_target[0]

            if bot_ele != bot_target[0] and top_ele == bot_target[0]:
                bottoms[idx] = bot_target[0]

        return min(len(tops) - top_target[1], len(bottoms) - bot_target[1]) if len(set(tops)) == 1 or len(set(bottoms)) == 1 else -1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minDominoRotations(tops = [2, 1, 2, 4, 2, 2], bottoms = [5, 2, 6, 2, 3, 2])
    assert test1 == 2
    
    test2 = sol.minDominoRotations(tops = [3, 5, 1, 2, 3], bottoms = [3, 6, 3, 3, 4])
    assert test2 == -1
    