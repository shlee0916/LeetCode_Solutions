'''
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/?envType=daily-question&envId=2024-05-29
'''

class Solution:
    def numSteps(self, s: str) -> int:
        length = len(s) - 1

        carry = 0
        ans = 0
        while length > 0:
            if int(s[length]) + carry == 0:
                carry = 0
                ans += 1
            elif int(s[length]) + carry == 2:
                carry = 1
                ans += 1
            else:
                carry = 1
                ans += 2
            
            length -= 1

        if carry == 1:
            ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numSteps(s = "1101")
    assert test1 == 6
    
    test2 = sol.numSteps(s = "10")
    assert test2 == 1
    
    test3 = sol.numSteps(s = "1")
    assert test3 == 0
    