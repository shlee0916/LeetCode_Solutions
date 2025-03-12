'''
https://leetcode.com/problems/remove-all-occurrences-of-a-substring/?envType=daily-question&envId=2025-02-11
'''

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = []
        
        for ch in s:
            ans.append(ch)
            while len(ans) >= len(part) and "".join(ans[-len(part):]) == part:
                ans[-len(part):] = ""

        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.removeOccurrences(s = "daabcbaabcbc", part = "abc")
    assert test1 == "dab"

    test2 = sol.removeOccurrences(s = "axxxxyyyyb", part = "xy")
    assert test2 == "ab"
    