'''
https://leetcode.com/problems/minimum-operations-to-make-array-equal/
'''

class Solution:
    def minOperations(self, n: int) -> int:
        return n * n // 4


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minOperations(3)
    assert test1 == 2

    test2 = sol.minOperations(6)
    assert test2 == 9
    