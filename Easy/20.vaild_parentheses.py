'''
https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = [ch for ch in s][::-1]
        while s:
            cur = s.pop()
            if stack:
                if stack[-1] == "(" and cur == ")":
                    stack.pop()
                elif  stack[-1] == "[" and cur == "]":
                    stack.pop()
                elif stack[-1] == "{" and cur == "}":
                    stack.pop()
                else:
                    stack.append(cur)
            else:
                stack.append(cur)
                
        if stack:
            return False
        else:
            return True
        

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isValid("()"), True)
    print(sol.isValid("()[]{}"), True)
    print(sol.isValid("(]"), False)