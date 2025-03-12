'''
https://leetcode.com/problems/happy-number/
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        nums = str(n)
        sums_set = set()
        while nums != "1":
            sums = sum(int(num) ** 2 for num in nums)
            if sums in sums_set:
                return False
            sums_set.add(sums)
            nums = str(sums)
            
        return True
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isHappy(2))
    print(sol.isHappy(10))
    print(sol.isHappy(7))
    print(sol.isHappy(30))