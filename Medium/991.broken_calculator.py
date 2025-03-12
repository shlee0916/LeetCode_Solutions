'''
https://leetcode.com/problems/broken-calculator/description/
'''

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        cnt = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            cnt += 1

        return cnt + (startValue - target)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.brokenCalc(startValue = 2, target = 3)
    assert test1 == 2
    
    test2 = sol.brokenCalc(startValue = 5, target = 8)
    assert test2 == 2
    
    test3 = sol.brokenCalc(startValue = 3, target = 10)
    assert test3 == 3
    