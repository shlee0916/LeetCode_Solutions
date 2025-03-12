'''
https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/?envType=daily-question&envId=2025-02-15
'''

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def checkit(num, target):
            if num == target:
                return True

            if num == 0:
                return target == 0

            for div in (10, 100, 1000):
                if checkit(num // div, target - num % div):
                    return True

            return False

        return sum(num * num for num in range(1, n + 1) if checkit(num * num, num)) 


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.punishmentNumber(n = 10)
    assert test1 == 182

    test2 = sol.punishmentNumber(n = 37)
    assert test2 == 1478
    