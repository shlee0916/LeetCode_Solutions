'''
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2023-12-24
'''

class Solution:
    def minOperations(self, s: str) -> int:
        start_with_one = 0
        start_with_zero = 0

        for idx, ch in enumerate(s):
            zero = str(idx % 2)
            
            start_with_one += ch != zero
            start_with_zero += ch == zero

        return min(start_with_one, start_with_zero) 


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minOperations(s = "0100")
    assert test1 == 1
    
    test2 = sol.minOperations(s = "10")
    assert test2 == 0
    
    test3 = sol.minOperations(s = "1111")
    assert test3 == 2
    