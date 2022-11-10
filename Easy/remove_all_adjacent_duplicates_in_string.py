'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.removeDuplicates("abbaca")
    print(test1, "ca")
    assert test1 == "ca"

    test2 = sol.removeDuplicates("azxxzy")
    print(test2, "ay")
    assert test2 == "ay"
