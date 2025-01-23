'''
https://leetcode.com/problems/bitwise-and-of-numbers-range/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift_cnt = 0

        while left != right:
            left >>= 1
            right >>= 1
            shift_cnt += 1

        return left << shift_cnt
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.rangeBitwiseAnd(left = 5, right = 7)
    assert test1 == 4

    test2 = sol.rangeBitwiseAnd(left = 0, right = 0)
    assert test2 == 0

    test3 = sol.rangeBitwiseAnd(left = 1, right = 2147483647)
    assert test3 == 0
    