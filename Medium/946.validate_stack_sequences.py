'''
https://leetcode.com/problems/validate-stack-sequences/description/
'''

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for num in pushed:
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
                
            if num == popped[0]:
                popped.pop(0)
            else:
                stack.append(num)

        for num in popped:
            if stack[-1] == num:
                stack.pop()

        return not stack


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.validateStackSequences(pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1])
    assert test1 == True

    test2 = sol.validateStackSequences(pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2])
    assert test2 == False
    