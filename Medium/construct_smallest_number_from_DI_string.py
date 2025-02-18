'''
https://leetcode.com/problems/construct-smallest-number-from-di-string/?envType=daily-question&envId=2025-02-18
'''

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        stack = []

        for idx, ch in enumerate(pattern + "I", 1):
            stack.append(str(idx))

            if ch == "I":
                ans.extend(stack[::-1][:])
                stack = []
        
        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.smallestNumber(pattern = "IIIDIDDD")
    assert test1 == "123549876"

    test2 = sol.smallestNumber(pattern = "DDD")
    assert test2 == "4321"
    