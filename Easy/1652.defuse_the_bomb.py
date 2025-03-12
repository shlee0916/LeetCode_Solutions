'''
https://leetcode.com/problems/defuse-the-bomb/?envType=daily-question&envId=2024-11-18
'''

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def __helper():
            ans = []
            idx = 1
            cur_sum = sum(circle_code[idx : idx + k])
            for _ in range(len(code)):
                ans.append(cur_sum)
                cur_sum -= circle_code[idx]
                cur_sum += circle_code[idx + k]
                idx += 1

            return ans


        circle_code = code * 2

        if k == 0:
            ans = [0] * len(code)

        elif k > 0:
            ans = __helper()

        elif k < 0:
            circle_code = circle_code[::-1]
            k = abs(k)
            ans = __helper()[::-1]

        return ans
            

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.decrypt(code = [5,7,1,4], k = 3)
    assert test1 == [12, 10, 16, 13]

    test2 = sol.decrypt(code = [1, 2, 3, 4], k = 0)
    assert test2 == [0, 0, 0, 0]

    test3 = sol.decrypt(code = [2, 4, 9, 3], k = -2)
    assert test3 == [12, 5, 6, 13]
    