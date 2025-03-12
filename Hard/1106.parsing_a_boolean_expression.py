'''
https://leetcode.com/problems/parsing-a-boolean-expression/description/
'''


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:
            if ch == ")":
                vals = set()
                while stack[-1] != "(":
                    vals.add(stack.pop())
                
                stack.pop()
                op = stack.pop()
                stack.append(all(vals) if op == "&" else any(vals) if op == "|" else not vals.pop())
            elif ch != ",":
                stack.append(True if ch == "t" else False if ch == "f" else ch)

        return stack.pop()
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.parseBoolExpr(expression = "&(|(f))")
    assert test1 == False
    
    test2 = sol.parseBoolExpr(expression = "|(f,f,f,t)")
    assert test2 == True
    
    test3 = sol.parseBoolExpr(expression = "!(&(f,t))")
    assert test3 == True
    