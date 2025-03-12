'''
https://leetcode.com/problems/largest-odd-number-in-string/description/?envType=daily-question&envId=2023-12-07
'''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for idx in range(len(num) - 1, -1, -1):
            if int(num[idx]) % 2 == 1:
                return num[:idx + 1]

        return ""


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.largestOddNumber(num = "52")
    assert test1 == "5"

    test2 = sol.largestOddNumber(num = "4206")
    assert test2 == ""

    test3 = sol.largestOddNumber(num = "35427")
    assert test3 == "35427"
    