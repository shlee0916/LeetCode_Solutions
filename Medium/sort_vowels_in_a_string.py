'''
https://leetcode.com/problems/sort-vowels-in-a-string/description/
'''

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for idx, ch in enumerate(s):
            if ch in "AEIOUaeiou":
                vowels.append(ord(ch))

        vowels.sort()
        vowels = vowels[::-1]

        new_str = ""
        for ch in s:
            if ch in "AEIOUaeiou":
                new_str += chr(vowels.pop())
            else:
                new_str += ch

        return new_str


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.sortVowels(s = "lEetcOde")
    assert test1 == "lEOtcede"

    test2 = sol.sortVowels(s = "lYmpH")
    assert test2 == "lYmpH"
    