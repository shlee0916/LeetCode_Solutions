'''
https://leetcode.com/problems/length-of-last-word/description/
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.lengthOfLastWord(s = "Hello World")
    assert test1 == 5
    
    test2 = sol.lengthOfLastWord(s = "   fly me   to   the moon  ")
    assert test2 == 4
    
    test3 = sol.lengthOfLastWord(s = "luffy is still joyboy")
    assert test3 == 6
    