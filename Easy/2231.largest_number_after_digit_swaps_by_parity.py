'''
https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/
'''

class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        ans = 0

        for ch in str(num):
            if int(ch) % 2 == 0:
                even.append(int(ch))
            else:
                odd.append(int(ch))

        odd.sort()
        even.sort()

        for ch in str(num):
            if int(ch) % 2 == 0:
                ans = ans * 10 + even.pop()
            else:
                ans = ans * 10 + odd.pop()

        return ans
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.largestInteger(num = 1234)
    assert test1 == 3412
    
    test2 = sol.largestInteger(num = 65875)
    assert test2 == 87655
    