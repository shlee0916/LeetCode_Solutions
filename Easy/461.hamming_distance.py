'''
https://leetcode.com/problems/hamming-distance/description/
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.hammingDistance(1, 4)
    print(test1, 2)
    assert test1 == 2
    
    test2 = sol.hammingDistance(3, 1)
    print(test2, 1)
    assert test2 == 1
    