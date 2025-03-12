'''
https://leetcode.com/problems/basic-calculator-ii/description/
'''
from math import trunc


class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        ans = 0
        tmp_res = 0
        prev_oper = "+"

        for ch in s + "##":
            if ch == " ":
                continue
            elif ch.isdigit():
                cur = cur * 10 + int(ch)
            else:
                if prev_oper == "*":
                    tmp_res *= cur
                elif prev_oper == "/":
                    tmp_res = trunc(tmp_res / cur)
                else:
                    ans += tmp_res
                    if prev_oper == "+":
                        tmp_res = cur
                    else:
                        tmp_res = -cur
                
                prev_oper, cur = ch, 0

        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.calculate("3+2*2")
    print(test1, 7)
    assert test1 == 7
    
    test2 = sol.calculate(" 3/2 ")
    print(test2, 1)
    assert test2 == 1
    
    test3 = sol.calculate(" 3+5 / 2 ")
    print(test3, 5)
    assert test3 == 5
    