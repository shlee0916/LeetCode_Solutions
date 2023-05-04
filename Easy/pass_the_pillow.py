'''
https://leetcode.com/problems/pass-the-pillow/description/
'''

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        share, remainder = divmod(time, n - 1)

        return n - remainder if share % 2 != 0 else 1 + remainder


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.passThePillow(n = 4, time = 5)
    assert test1 == 2
    
    test2 = sol.passThePillow(n = 3, time = 2)
    assert test2 == 3
    