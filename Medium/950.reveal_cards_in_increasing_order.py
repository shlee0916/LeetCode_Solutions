'''
https://leetcode.com/problems/reveal-cards-in-increasing-order/description/
'''

from collections import deque

from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = deque()

        for card in sorted(deck)[::-1]:
            ans.rotate()
            ans.appendleft(card)

        return list(ans)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.deckRevealedIncreasing(deck = [17, 13, 11, 2, 3, 5, 7])
    assert test1 == [2, 13, 3, 11, 5, 17, 7]

    test2 = sol.deckRevealedIncreasing(deck = [1, 1000])
    assert test2 == [1, 1000]
    