'''
https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10
'''

class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for ch in s:
            if ans and ch.isdigit():
                ans.pop()
            else:
                ans.append(ch)

        return "".join(ans)
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.clearDigits(s = "abc")
    assert test1 == "abc"

    test2 = sol.clearDigits(s = "cb34")
    assert test2 == ""
    