'''
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for ch in s:
            if ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        return len(stack)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minAddToMakeValid(s = "())")
    assert test1 == 1

    test2 = sol.minAddToMakeValid(s = "(((")
    assert test2 == 3
