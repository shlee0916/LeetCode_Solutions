'''
https://leetcode.com/problems/delete-characters-to-make-fancy-string/?envType=daily-question&envId=2024-11-01
'''

class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for ch in s:
            if len(stack) > 1 and stack[-2] == stack[-1] == ch:
                pass
            else:
                stack.append(ch)

        return "".join(stack)
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.makeFancyString(s = "leeetcode")
    assert test1 == "leetcode"

    test2 = sol.makeFancyString(s = "aaabaaaa")
    assert test2 == "aabaa"

    test3 = sol.makeFancyString(s = "aab")
    assert test3 == "aab"
    