'''
https://leetcode.com/problems/fraction-addition-and-subtraction/?envType=daily-question&envId=2024-08-23
'''

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b

            return a


        exp = expression.replace("+", " +").replace("-", " -")
        fractions = exp.split()

        ans_num = 0
        ans_dom = 1
        for frac in fractions:
            num, dom = map(int, frac.split("/"))

            ans_num = (ans_num * dom) + (num * ans_dom)
            ans_dom *= dom

            cur_gcd = gcd(ans_num, ans_dom)
            ans_num /= cur_gcd
            ans_dom /= cur_gcd

        return f"{int(ans_num)}/{int(ans_dom)}"


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.fractionAddition(expression = "-1/2+1/2")
    assert test1 == "0/1"

    test2 = sol.fractionAddition(expression = "-1/2+1/2+1/3")
    assert test2 == "1/3"

    test3 = sol.fractionAddition(expression = "1/3-1/2")
    assert test3 == "-1/6"
    