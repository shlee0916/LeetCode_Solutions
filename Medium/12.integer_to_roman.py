'''
https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_table = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        roman_str = ""
        for roman_num in list(roman_table.keys())[::-1]:
            roman_str += (num // roman_num) * roman_table[roman_num]
            num %= roman_num

        return roman_str


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.intToRoman(num = 3)
    assert test1 == "III"

    test2 = sol.intToRoman(num = 58)
    assert test2 == "LVIII"

    test3 = sol.intToRoman(num = 1994)
    assert test3 == "MCMXCIV"
    