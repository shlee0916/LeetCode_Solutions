'''
https://leetcode.com/problems/ugly-number/description/
'''

class Solution:
    def isUgly(self, num: int) -> bool:
        for prime in 2, 3, 5:
            while num % prime == 0 < num:
                num /= prime

        return num == 1


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.isUgly(6)
    print(test1, True)
    assert test1 == True

    test2 = sol.isUgly(1)
    print(test2, True)
    assert test2 == True

    test3 = sol.isUgly(14)
    print(test3, False)
    assert test3 == False
