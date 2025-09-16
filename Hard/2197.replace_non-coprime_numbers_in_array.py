'''
https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description/?envType=daily-question&envId=2025-09-16
'''

from typing import List


class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b > 0:
            a, b = b, a % b
        return a


    def lcm(self, a, b):
        return a * b / self.gcd(a, b)


    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1 and self.gcd(stack[-1], stack[-2]) > 1:
                stack.append(int(self.lcm(stack.pop(), stack.pop())))

        return stack


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.replaceNonCoprimes(nums = [6, 4, 3, 2, 7, 6, 2])
    assert test1 == [12, 7, 6]

    test2 = sol.replaceNonCoprimes(nums = [2, 2, 1, 1, 3, 3, 3])
    assert test2 == [2, 1, 1, 3]
