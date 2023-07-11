'''
https://leetcode.com/problems/lemonade-change/description/
'''

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                changes[10] += 1
                changes[5] -= 1
            elif changes[10] > 0:
                changes[10] -= 1
                changes[5] -= 1
            else:
                changes[5] -= 3

            if changes[5] < 0:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.lemonadeChange(bills = [5, 5, 5, 10, 20])
    assert test1 == True
    
    test2 = sol.lemonadeChange(bills = [5, 5, 10, 10, 20])
    assert test2 == False
    