'''
https://leetcode.com/problems/backspace-string-compare/description/
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(word: str):
            stack = []
            for ch in word:
                if stack and ch == "#":
                    stack.pop()
                elif ch != "#":
                    stack.append(ch)

            return "".join(stack)

        return backspace(s) == backspace(t)
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.backspaceCompare(s = "ab#c", t = "ad#c")
    assert test1 == True

    test2 = sol.backspaceCompare(s = "ab##", t = "c#d#")
    assert test2 == True

    test3 = sol.backspaceCompare(s = "a#c", t = "b")
    assert test3 == False
