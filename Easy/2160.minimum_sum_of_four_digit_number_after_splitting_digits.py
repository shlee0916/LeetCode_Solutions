'''
https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
'''

class Solution:
    def minimumSum(self, num: int) -> int:
        numbers = sorted(str(num))

        return (int(numbers[0]) + int(numbers[1])) * 10 + int(numbers[2]) + int(numbers[3])


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumSum(num = 2932)
    assert test1 == 52

    test2 = sol.minimumSum(num = 4009)
    assert test2 == 13
