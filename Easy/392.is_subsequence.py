'''
https://leetcode.com/problems/is-subsequence/description/
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True

        target_idx = 0
        for ch in t:
            if target_idx <= len(s) - 1 and s[target_idx] == ch:
                target_idx += 1

        return target_idx == len(s)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isSubsequence(s = "abc", t = "ahbgdc")
    print(test1, True)
    assert test1 == True
    
    test2 = sol.isSubsequence(s = "axc", t = "ahbgdc")
    print(test2, False)
    assert test2 == False
    