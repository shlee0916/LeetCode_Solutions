'''
https://leetcode.com/problems/minimum-string-length-after-removing-substrings/?envType=daily-question&envId=2024-10-07
'''

class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for ch in s:
            if stack and ch == "B" and stack[-1] == "A":
                stack.pop()
            elif stack and ch == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minLength(s = "ABFCACDB")
    assert test1 == 2

    test2 = sol.minLength(s = "ACBBD")
    assert test2 == 5
    