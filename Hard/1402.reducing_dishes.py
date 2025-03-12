'''
https://leetcode.com/problems/reducing-dishes/description/
'''

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)

        pre, result = 0, 0
        for sat in satisfaction:
            pre += sat
            if pre < 0:
                break

            result += pre

        return result
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxSatisfaction(satisfaction = [-1, -8, 0, 5, -9])
    print(test1, 14)
    assert test1 == 14

    test2 = sol.maxSatisfaction(satisfaction = [4, 3, 2])
    print(test2, 20)
    assert test2 == 20

    test3 = sol.maxSatisfaction(satisfaction = [-1, -4, -5])
    print(test3, 0)
    assert test3 == 0
