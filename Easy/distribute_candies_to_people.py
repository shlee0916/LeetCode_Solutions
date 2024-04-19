'''
https://leetcode.com/problems/distribute-candies-to-people/
'''

from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        give_candy = 0

        while candies > 0:
            ans[give_candy % num_people] += min(give_candy + 1, candies)
            give_candy += 1
            candies -= give_candy

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.distributeCandies(candies = 7, num_people = 4)
    assert test1 == [1, 2, 3, 1]
    
    test2 = sol.distributeCandies(candies = 10, num_people = 3)
    assert test2 == [5, 2, 3]
    