'''
https://leetcode.com/problems/remove-outermost-parentheses/
'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        opened = 0

        for ch in s:
            if ch == "(" and opened > 0:
                ans += ch
            if ch == ")" and opened > 1:
                ans += ch

            if ch == "(":
                opened += 1
            else:
                opened -= 1
        
        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.removeOuterParentheses(s = "(()())(())")
    assert test1 == "()()()"
    
    test2 = sol.removeOuterParentheses(s = "(()())(())(()(()))")
    assert test2 == "()()()()(())"
    
    test3 = sol.removeOuterParentheses(s = "()()")
    assert test3 == ""
    