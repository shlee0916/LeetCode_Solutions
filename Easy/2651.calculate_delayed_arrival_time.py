'''
https://leetcode.com/problems/calculate-delayed-arrival-time/
'''

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


if __name__ == "__main__":
    sol = Solution()
    
    test1= sol.findDelayedArrivalTime(arrivalTime = 15, delayedTime = 5)
    assert test1 == 20
    
    test2 = sol.findDelayedArrivalTime(arrivalTime = 13, delayedTime = 11)
    assert test2 == 0
    