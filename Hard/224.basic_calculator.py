'''
https://leetcode.com/problems/basic-calculator/description/
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        res = 0
        cur_digit = 0
        sign = 1

        for ch in s + "+":
            if ch == " ":
                continue
            elif ch.isdigit():
                cur_digit = (cur_digit * 10) + int(ch)
            elif ch in "+-":
                res += cur_digit * sign * stack[-1]
                sign = 1 if ch == "+" else -1
                cur_digit = 0
            elif ch == "(":
                stack.append(sign * stack[-1])
                sign = 1
            elif ch == ")":
                res += cur_digit * sign * stack.pop()
                cur_digit = 0

        return res


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.calculate("1 + 1")
    print(test1, 2)
    assert test1 == 2
    
    test2 = sol.calculate(" 2-1 + 2 ")
    print(test2, 3)
    assert test2 == 3
    
    test3 = sol.calculate("(1+(4+5+2)-3)+(6+8)")
    print(test3, 23)
    assert test3 == 23
    