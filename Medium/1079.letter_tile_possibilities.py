'''
https://leetcode.com/problems/letter-tile-possibilities/description/
'''

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        
        stack = [("", tiles)]
        while stack:
            cur_str, next_str = stack.pop()

            if cur_str:
                result.add(cur_str)
            
            for idx in range(len(next_str)):
                stack.append((cur_str + next_str[idx], next_str[:idx] + next_str[idx + 1:]))

        return len(result)
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numTilePossibilities(tiles = "AAB")
    assert test1 == 8

    test2 = sol.numTilePossibilities(tiles = "AAABBC")
    assert test2 == 188

    test3 = sol.numTilePossibilities(tiles = "V")
    assert test3 == 1
    