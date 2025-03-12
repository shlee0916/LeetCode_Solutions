'''
https://leetcode.com/problems/decoded-string-at-index/description/?envType=daily-question&envId=2023-09-27
'''

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_length = 0

        for ch in s:
            if ch.isdigit():
                total_length *= int(ch)
            else:
                total_length += 1

        for idx, ch in enumerate(s[::-1]):
            idx = len(s) - idx - 1

            if ch.isdigit():
                total_length /= int(ch)
                k %= total_length
            else:
                if k == 0 or k == total_length:
                    return ch

                total_length -= 1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.decodeAtIndex(s = "leet2code3", k = 10)
    assert test1 == "o"

    test2 = sol.decodeAtIndex(s = "ha22", k = 5)
    assert test2 == "h"

    test3 = sol.decodeAtIndex(s = "a2345678999999999999999", k = 1)
    assert test3 == "a"
    