'''
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/?envType=daily-question&envId=2024-07-11
'''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for ch in s:
            if ch == "(":
                stack.append("")

            elif ch == ")":
                tmp_str = stack.pop()[::-1]
                stack[-1] += tmp_str

            else:
                stack[-1] += ch

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.reverseParentheses(s = "(abcd)")
    assert test1 == "dcba"

    test2 = sol.reverseParentheses(s = "(u(love)i)")
    assert test2 == "iloveu"

    test3 = sol.reverseParentheses(s = "(ed(et(oc))el)")
    assert test3 == "leetcode"
    