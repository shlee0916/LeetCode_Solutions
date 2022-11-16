'''
https://leetcode.com/problems/guess-number-higher-or-lower/description/
'''

def guess(number: int) -> int:
    if number == picked:
        return 0
    elif number < picked:
        return 1
    elif number > picked:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        
        start = 1
        end = n

        while start <= end:
            number = (start + end) // 2

            guessing = guess(number)
            if guessing == 0:
                return number
            elif guessing == 1:
                start = number + 1
            else:
                end = number - 1


if __name__ == "__main__":
    sol = Solution()

    picked = 6
    test1 = sol.guessNumber(10)
    print(test1, 6)
    assert test1 == 6

    picked = 1
    test2 = sol.guessNumber(1)
    print(test2, 1)
    assert test2 == 1

    picked = 1
    test3 = sol.guessNumber(2)
    print(test3, 1)
    assert test3 == 1
    