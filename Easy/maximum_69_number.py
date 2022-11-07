'''
https://leetcode.com/problems/maximum-69-number/description/
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximum69Number(9669)
    print(test1, 9969)
    assert test1 == 9969

    test2 = sol.maximum69Number(9996)
    print(test2, 9999)
    assert test2 == 9999

    test3 = sol.maximum69Number(9999)
    print(test3, 9999)
    assert test3 == 9999