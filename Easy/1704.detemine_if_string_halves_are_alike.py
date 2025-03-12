'''
https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        front, back = s[:len(s) // 2], s[len(s) // 2:]

        return sum([1 for ch in front if ch in "aeiouAEIOU"]) == sum([1 for ch in back if ch in "aeiouAEIOU"])


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.halvesAreAlike("book")
    print(test1, True)
    assert test1 == True

    test2 = sol.halvesAreAlike("textbook")
    print(test2, False)
    assert test2 == False
