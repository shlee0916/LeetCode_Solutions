'''
https://leetcode.com/problems/removing-stars-from-a-string/description/
'''

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and ch == "*":
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.removeStars(s = "leet**cod*e")
    assert test1 == "lecoe"

    test2 = sol.removeStars(s = "erase*****")
    assert test2 == ""
    