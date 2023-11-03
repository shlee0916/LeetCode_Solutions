'''
https://leetcode.com/problems/score-of-parentheses/description/
'''

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        cur = 0

        for ch in s:
            if ch == "(":
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)

        return cur
    
    
if __name__ == "__main__":
    sol = Solution()

    test1 = sol.scoreOfParentheses(s = "()")
    assert test1 == 1

    test2 = sol.scoreOfParentheses(s = "(())")
    assert test2 == 2

    test3 = sol.scoreOfParentheses(s = "()()")
    assert test3 == 2
    