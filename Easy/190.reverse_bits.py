'''
https://leetcode.com/problems/reverse-bits/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = bin(n)
        bin_str = bin_str[2:]
        bin_str = bin_str[::-1] + ("0" * (32 - len(bin_str)))

        return int(bin_str, 2)


if __name__ == "__main__":
    sol = Solution()
 
    test1 = sol.reverseBits(n = 43261596) # 00000010100101000001111010011100
    assert test1 == 964176192 # 00111001011110000010100101000000

    test2 = sol.reverseBits(n = 4294967293) # 11111111111111111111111111111101
    assert test2 == 3221225471 # 10111111111111111111111111111111
