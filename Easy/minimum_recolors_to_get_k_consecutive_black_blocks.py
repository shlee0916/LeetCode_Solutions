'''
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float("inf")
        for idx in range(len(blocks) - k + 1):
            white = blocks.count("W", idx, idx + k)
            ans = min(white, ans)

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minimumRecolors(blocks = "WBBWWBBWBW", k = 7)
    assert test1 == 3
    
    test2 = sol.minimumRecolors(blocks = "WBWBBBW", k = 2)
    assert test2 == 0
    