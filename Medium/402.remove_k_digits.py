'''
https://leetcode.com/problems/remove-k-digits/?envType=daily-question&envId=2024-04-25
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numbers = []
        for n in num:
            while numbers and k and numbers[-1] > n:
                numbers.pop()
                k -= 1

            if numbers or n != "0":
                numbers.append(n)

        if k:
            numbers = numbers[:-k]

        return "".join(numbers) or "0"


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.removeKdigits(num = "1432219", k = 3)
    assert test1 == "1219"
    
    test2 = sol.removeKdigits(num = "10200", k = 1)
    assert test2 == "200"
    
    test3 = sol.removeKdigits(num = "10", k = 2)
    assert test3 == "0"
