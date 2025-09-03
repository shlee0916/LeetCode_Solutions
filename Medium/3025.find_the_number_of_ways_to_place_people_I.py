from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p: (p[0], -p[1]))
        ans = 0

        for idx in range(len(points)):
            upper_y = points[idx][1]
            lower_y_limit = float("-inf")

            for n_idx in range(idx + 1, len(points)):
                cur_y = points[n_idx][1]
                if cur_y <= upper_y and cur_y > lower_y_limit:
                    ans += 1
                    lower_y_limit = cur_y
                    if cur_y == upper_y:
                        break
        
        return ans


if __name__ == "__main__":
    sol = Solution() 

    test1 = sol.numberOfPairs(points = [[1, 1], [2, 2], [3, 3]])
    assert test1 == 0

    test2 = sol.numberOfPairs(points = [[6, 2], [4, 4], [2, 6]])
    assert test2 == 2

    test3 = sol.numberOfPairs(points = [[3, 1], [1, 3], [1, 1]])
    assert test3 == 2
