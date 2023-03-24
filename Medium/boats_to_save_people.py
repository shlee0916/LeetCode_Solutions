'''
https://leetcode.com/problems/boats-to-save-people/https://leetcode.com/problems/boats-to-save-people/
'''

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boat, begin, end = 0, 0, len(people) - 1
        while begin <= end:
            if people[begin] + people[end] <= limit:
                begin += 1
            boat += 1
            end -= 1

        return boat
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numRescueBoats(people = [1, 2], limit = 3)
    print(test1, 1)
    assert test1 == 1
    
    test2 = sol.numRescueBoats(people = [3, 2, 2, 1], limit = 3)
    print(test2, 3)
    assert test2 == 3
    
    test3 = sol.numRescueBoats(people = [3, 5, 3, 4], limit = 5)
    print(test3, 4)
    assert test3 == 4
    