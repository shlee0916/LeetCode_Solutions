'''
https://leetcode.com/problems/number-complement/?envType=daily-question&envId=2024-08-22
'''

class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask <= num:
            mask = mask << 1

        return (mask - 1) ^ num
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findComplement(num = 5)
    assert test1 == 2

    test2 = sol.findComplement(num = 1)
    assert test2 == 0
    