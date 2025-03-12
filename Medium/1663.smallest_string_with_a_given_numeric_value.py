'''
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/description/
'''

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ["a"] * n
        idx = n - 1
        k -= n

        while k != 0:
            k += 1
            if k / 26 >= 1:
                res[idx] = "z"
                k -= 26
                idx -= 1
            else:
                res[idx] = chr(k + 96)
                k = 0

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.getSmallestString(n = 3, k = 27)
    assert test1 == "aay"
    
    test2 = sol.getSmallestString(n = 5, k = 73)
    assert test2 == "aaszz"
    