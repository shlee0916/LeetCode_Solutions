'''
https://leetcode.com/problems/hand-of-straights/description/?envType=daily-question&envId=2024-06-06
'''

from collections import Counter

from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cards = Counter(hand)

        for card in sorted(cards.keys()):
            if cards[card] > 0:
                for next_one in range(groupSize)[::-1]:
                    cards[card + next_one] -= cards[card]
                    if cards[card + next_one] < 0:
                        return False

        return True


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isNStraightHand(hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3)
    assert test1 == True
    
    test2 = sol.isNStraightHand(hand = [1, 2, 3, 4, 5], groupSize = 4)
    assert test2 == False
    