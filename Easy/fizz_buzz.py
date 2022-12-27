'''
https://leetcode.com/problems/fizz-buzz/description/
'''

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for idx, word in enumerate(range(1, n + 1)):
            if word % 3 == 0 and word % 5 == 0:
                ans.append("FizzBuzz")
            elif word % 3 == 0:
                ans.append("Fizz")
            elif word % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(f"{idx + 1}")

        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.fizzBuzz(n = 3)
    print(test1, ["1", "2", "Fizz"])
    assert test1 == ["1", "2", "Fizz"]
    
    test2 = sol.fizzBuzz(n = 5)
    print(test2, ["1", "2", "Fizz", "4", "Buzz"])
    assert test2 == ["1", "2", "Fizz", "4", "Buzz"]
    
    test3 = sol.fizzBuzz(n = 15)
    print(test3, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
    assert test3 == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    