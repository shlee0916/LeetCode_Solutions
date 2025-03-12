'''
https://leetcode.com/problems/water-bottles/description/
'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        cur_water_bottle = numBottles

        while cur_water_bottle >= numExchange:
            cur_water_bottle, remainder = divmod(cur_water_bottle, numExchange)
            ans += cur_water_bottle
            cur_water_bottle += remainder

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numWaterBottles(numBottles = 9, numExchange = 3)
    assert test1 == 13
    
    test2 = sol.numWaterBottles(numBottles = 15, numExchange = 4)
    assert test2 == 19
    