'''
https://leetcode.com/problems/knight-dialer/description/?envType=daily-question&envId=2023-11-27
'''

class Solution:
    def knightDialer(self, n: int) -> int:
        next_digits = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: tuple(),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)
        }

        current_state = [1] * 10
        for _ in range(n - 1):
            next_state = [0] * 10

            for num in range(10):
                for next_digit in next_digits[num]:
                    next_state[next_digit] = (next_state[next_digit] + current_state[num]) % (10 ** 9 + 7)

            current_state = next_state
        
        return sum(current_state) % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.knightDialer(n = 1)
    assert test1 == 10

    test2 = sol.knightDialer(n = 2)
    assert test2 == 20

    test3 = sol.knightDialer(n = 3131)
    assert test3 == 136006598
    