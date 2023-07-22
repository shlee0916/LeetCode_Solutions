'''
https://leetcode.com/problems/time-needed-to-buy-tickets/submissions/
'''

from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        idx = 0

        while tickets[k] != 0:
            if tickets[idx] != 0:
                tickets[idx] -= 1
                ans += 1

            idx = (idx + 1) % len(tickets)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.timeRequiredToBuy(tickets = [2, 3, 2], k = 2)
    assert test1 == 6
    
    test2 = sol.timeRequiredToBuy(tickets = [5, 1, 1, 1], k = 0)
    assert test2 == 8
    