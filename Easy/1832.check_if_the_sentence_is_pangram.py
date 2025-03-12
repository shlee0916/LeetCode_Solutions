'''
https://leetcode.com/problems/check-if-the-sentence-is-pangram/
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = "abcdefghijklmnopqrstwuvxyz"
        
        for ch in sentence:
            alphabets = alphabets.replace(ch, "")
        
        return not alphabets


if __name__ == "__main__":
    sol = Solution()

    print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"), True)
    print(sol.checkIfPangram("leetcode"), False)