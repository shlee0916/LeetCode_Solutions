'''
https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x

        while True:
            mid = left + (right - left) // 2

            if mid > x / mid:
                right = mid - 1
            else:
                if mid + 1 > x / (mid + 1):
                    return mid

                left = mid + 1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.mySqrt(x = 4)
    assert test1 == 2
    
    test2 = sol.mySqrt(x = 8)
    assert test2 == 2
    