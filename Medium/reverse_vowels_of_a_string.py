'''
https://leetcode.com/problems/reverse-vowels-of-a-string/description/
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)
        left, right = 0, len(s) - 1
        while left <= right:
            while left <= right and s[left] not in vowels: left += 1
            while left <= right and s[right] not in vowels: right -= 1

            if left > right:
                break

            s[left], s[right] = s[right], s[left]

            left, right = left + 1, right - 1

        return "".join(s)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.reverseVowels("hello")
    print(test1, "holle")
    assert test1 == "holle"

    test2 = sol.reverseVowels("leetcode")
    print(test2, "leotcede")
    assert test2 == "leotcede"