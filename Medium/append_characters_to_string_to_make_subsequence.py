'''
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/
'''

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_pointer = 0
        t_pointer = 0

        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                t_pointer += 1
                s_pointer += 1
            else:
                s_pointer += 1

        return len(t) - t_pointer


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.appendCharacters(s = "coaching", t = "coding")
    assert test1 == 4
    
    test2 = sol.appendCharacters(s = "abcde", t = "a")
    assert test2 == 0
    
    test3 = sol.appendCharacters(s = "z", t = "abcde")
    assert test3 == 5
    