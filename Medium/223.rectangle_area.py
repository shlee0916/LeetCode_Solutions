'''
https://leetcode.com/problems/rectangle-area/description/
'''

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = abs(ax1 - ax2) * abs(ay1 - ay2)
        area2 = abs(bx1 - bx2) * abs(by1 - by2)

        width = min(ax2, bx2) - max(ax1, bx1)
        height = min(ay2, by2) - max(ay1, by1)

        if width <= 0 or height <=0:
            return area1 + area2
        else:
            return area1 + area2 - (width * height)

        
if __name__ == "__main__":
    sol = Solution()

    test1 = sol.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2)
    print(test1, 45)
    assert test1 == 45

    test2 = sol.computeArea(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2)
    print(test2, 16)
    assert test2 == 16
