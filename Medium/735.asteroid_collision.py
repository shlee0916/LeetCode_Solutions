'''
https://leetcode.com/problems/asteroid-collision/description/
'''

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for ast in asteroids:
            while res and ast < 0 and res[-1] > 0:
                collision = res[-1] + ast

                if collision <= 0:
                    res.pop()
                if collision >= 0:
                    break

            else:
                res.append(ast)

        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.asteroidCollision(asteroids = [5, 10, -5])
    assert test1 == [5, 10]

    test2 = sol.asteroidCollision(asteroids = [8, -8])
    assert test2 == []

    test3 = sol.asteroidCollision(asteroids = [10, 2, -5])
    assert test3 == [10]
    