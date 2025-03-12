'''
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1

            steps += 1

        return steps


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numberOfSteps(num = 14)
    assert test1 == 6
    
    test2 = sol.numberOfSteps(num = 8)
    assert test2 == 4
    
    test3 = sol.numberOfSteps(num = 123)
    assert test3 == 12
    