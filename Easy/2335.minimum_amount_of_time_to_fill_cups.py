'''
https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
'''

from heapq import heapify, heappop, heappush

from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0

        new_amount = [-amt for amt in amount if amt != 0]
        heapify(new_amount)

        while new_amount:
            if len(new_amount) > 1:
                first_cup = heappop(new_amount) + 1
                second_cup = heappop(new_amount) + 1

                if first_cup < 0:
                    heappush(new_amount, first_cup)
                if second_cup < 0:
                    heappush(new_amount, second_cup)

                ans += 1

            else:
                new_cup = heappop(new_amount) + 1
                if new_cup < 0:
                    heappush(new_amount, new_cup)
                
                ans += 1

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.fillCups(amount = [1, 4, 2])
    assert test1 == 4
    
    test2 = sol.fillCups(amount = [5, 4, 4])
    assert test2 == 7
    
    test3 = sol.fillCups(amount = [5, 0, 0])
    assert test3 == 5
    