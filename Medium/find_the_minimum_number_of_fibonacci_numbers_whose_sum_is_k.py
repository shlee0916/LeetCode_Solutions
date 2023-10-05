'''
https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/description/
'''

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibo = [1, 1]

        while fibo[-1] <= k:
            fibo.append(fibo[-1] + fibo[-2])

        cnt = 0
        target = k
        while fibo and target > 0:
            cur_num = fibo.pop()
            if cur_num <= target:
                cnt += target // cur_num
                target %= cur_num
        
        return cnt
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findMinFibonacciNumbers(k = 7)
    assert test1 == 2

    test2 = sol.findMinFibonacciNumbers(k = 10)
    assert test2 == 2

    test3 = sol.findMinFibonacciNumbers(k = 19)
    assert test3 == 3
