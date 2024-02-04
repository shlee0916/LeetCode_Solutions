'''
https://leetcode.com/problems/add-digits/description/
'''

class Solution:
    def addDigits(self, num: int) -> int:
        nums = [int(num) for num in str(num)]

        while len(nums) != 1:
            nums = [int(num) for num in str(sum(nums))]

        return nums[0]
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.addDigits(num = 38)
    assert test1 == 2
    
    test2 = sol.addDigits(num = 0)
    assert test2 == 0
    