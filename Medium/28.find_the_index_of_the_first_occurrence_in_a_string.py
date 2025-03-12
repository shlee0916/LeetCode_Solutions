'''
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack)):
            if idx + len(needle) - 1 > len(haystack):
                break

            if haystack[idx:idx + len(needle)] == needle:
                return idx


        return -1


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.strStr(haystack = "sadbutsad", needle = "sad")
    print(test1, 0)
    assert test1 == 0

    test2 = sol.strStr(haystack = "leetcode", needle = "leeto")
    print(test2, -1)
    assert test2 == -1
    