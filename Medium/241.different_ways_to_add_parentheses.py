'''
https://leetcode.com/problems/different-ways-to-add-parentheses/description/
'''

from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []

        if expression.isdigit():
            return [eval(expression)]

        for idx, char in enumerate(expression):
            if char in "-+*":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])

                for l in left:
                    for r in right:
                        res.append(eval(str(l) + char + str(r)))

        return res


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.diffWaysToCompute(expression = "2-1-1")
    print(test1, [0, 2])
    assert sorted(test1) == [0, 2]

    test2 = sol.diffWaysToCompute(expression = "2*3-4*5")
    print(test2, [-34, -14, -10, -10, 10])
    assert sorted(test2) == [-34, -14, -10, -10, 10]
