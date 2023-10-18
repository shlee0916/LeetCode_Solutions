'''
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
'''

class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for ch in s:
            if stack and ch == "]":
                stack.pop()
            elif ch == "[":
                stack.append(ch)

        return (len(stack) + 1) // 2


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minSwaps(s = "][][")
    assert test1 == 1

    test2 = sol.minSwaps(s = "]]][[[")
    assert test2 == 2

    test3 = sol.minSwaps(s = "[]")
    assert test3 == 0
    