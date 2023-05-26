'''
https://leetcode.com/problems/jewels-and-stones/description/
'''

from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        all_jewels = Counter(stones)

        for jewel in jewels:
            cnt += all_jewels.get(jewel, 0)
        
        return cnt
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numJewelsInStones(jewels = "aA", stones = "aAAbbbb")
    assert test1 == 3
    
    test2 = sol.numJewelsInStones(jewels = "z", stones = "ZZ")
    assert test2 == 0
    