'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
from typing import List


class Solution:
    def evalRPN(self,  tokens: List[str]) -> int:
        nums = []
        
        while tokens:
            token = tokens.pop(0)
            if token in "+-*/":
                num1 = nums.pop()
                num2 = nums.pop()
                
                if token == "+":
                    nums.append(num1 + num2)
                elif token == "-":
                    nums.append(num2 - num1)
                elif token == "*":
                    nums.append(num1 * num2)
                elif token == "/":
                    nums.append(int(num2 / num1))
            else:
                nums.append(int(token))
                
        return nums[0]


if __name__ == "__main__":
    sol = Solution()

    print(sol.evalRPN(["2", "1", "+", "3", "*"]), 9)
    print(sol.evalRPN(["4", "13", "5", "/", "+"]), 6)
    print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)