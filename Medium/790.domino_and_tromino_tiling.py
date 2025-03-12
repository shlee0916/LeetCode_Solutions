'''
https://leetcode.com/problems/domino-and-tromino-tiling/description/
'''

class Solution:
    def numTilings(self, n: int) -> int:
        first_tile, second_tile, third_tile = 0, 1, 1

        for _ in range(n - 1):
            first_tile, second_tile, third_tile = second_tile, third_tile, (2 * third_tile + first_tile) % int(1e9 + 7)

        return third_tile
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numTilings(3)
    print(test1, 5)
    assert test1 == 5
    
    test2 = sol.numTilings(1)
    print(test2, 1)
    assert test2 == 1
    