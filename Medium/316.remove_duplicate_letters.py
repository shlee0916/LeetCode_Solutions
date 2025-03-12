'''
https://leetcode.com/problems/remove-duplicate-letters/description/?envType=daily-question&envId=2023-09-26
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = {}
        stack = []
        used = set()

        for idx, ch in enumerate(s):
            last_idx[ch] = idx

        for idx, ch in enumerate(s):
            if ch not in used:
                while stack and stack[-1] > ch and last_idx[stack[-1]] > idx:
                    used.remove(stack.pop())

                stack.append(ch)
                used.add(ch)

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.removeDuplicateLetters(s = "bcabc")
    assert test1 == "abc"
    
    test2 = sol.removeDuplicateLetters(s = "cbacdcbc")
    assert test2 == "acdb"
    