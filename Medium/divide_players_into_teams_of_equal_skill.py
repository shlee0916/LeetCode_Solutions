'''
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
'''

from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        target = sum(skill) / (len(skill) / 2)

        skill.sort()
        left = 0
        right = len(skill) - 1

        ans = 0
        while left < right:
            if skill[left] + skill[right] == target:
                ans += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.dividePlayers(skill = [3, 2, 5, 1, 3, 4])
    assert test1 == 22

    test2 = sol.dividePlayers(skill = [3, 4])
    assert test2 == 12

    test3 = sol.dividePlayers(skill = [1, 1, 2, 3])
    assert test3 == -1
    