'''
https://leetcode.com/problems/ransom-note/
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in magazine:
            if ch in ransomNote:
                ransomNote = ransomNote.replace(ch, "", 1)
                
        return False if ransomNote else True


if __name__ == "__main__":
    sol = Solution()

    print(sol.canConstruct("ab", "aab"), True)