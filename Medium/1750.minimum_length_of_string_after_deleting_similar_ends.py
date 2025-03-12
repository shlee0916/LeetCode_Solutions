'''
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/?envType=daily-question&envId=2024-03-05
'''

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0 
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            ch = s[left]
            while left <= right and s[left] == ch:
                left += 1

            while left <= right and s[right] == ch:
                right -= 1

        return right - left + 1
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumLength(s = "ca")
    assert test1 == 2

    test2 = sol.minimumLength(s = "cabaabac")
    assert test2 == 0

    test3 = sol.minimumLength(s = "aabccabba")
    assert test3 == 3
    