'''
https://leetcode.com/problems/make-the-string-great/description/
'''

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == chr(ord(ch) ^ 32):
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.makeGood("leEeetcode")
    print(test1, "leetcode")
    assert test1 == "leetcode"

    test2 = sol.makeGood("abBAcC")
    print(test2, "")
    assert test2 == ""

    test3 = sol.makeGood("s")
    print(test3, "s")
    assert test3 == "s"

    test4 = sol.makeGood("Pp")
    print(test4, "")
    assert test4 == ""