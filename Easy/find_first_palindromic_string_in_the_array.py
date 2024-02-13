'''
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/?envType=daily-question&envId=2024-02-13
'''

from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ""
        for word in words:
            if word == word[::-1]:
                ans = word
                break

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.firstPalindrome(words = ["abc", "car", "ada", "racecar", "cool"])
    assert test1 == "ada"

    test2 = sol.firstPalindrome(words = ["notapalindrome", "racecar"])
    assert test2 == "racecar"

    test3 = sol.firstPalindrome(words = ["def", "ghi"])
    assert test3 == ""
