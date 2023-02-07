'''
https://leetcode.com/problems/fruit-into-baskets/submissions/893291390/
'''

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start_idx, count = 0, {}

        for end_idx, fruit in enumerate(fruits):
            count[fruit] = count.get(fruit, 0) + 1

            if len(count) > 2:
                count[fruits[start_idx]] -= 1
                if count[fruits[start_idx]] == 0:
                    count.pop(fruits[start_idx])
                start_idx += 1

        return end_idx - start_idx + 1
            

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.totalFruit(fruits = [1, 2, 1])
    print(test1, 3)
    assert test1 == 3

    test2 = sol.totalFruit(fruits = [0, 1, 2, 2])
    print(test2, 3)
    assert test2 == 3

    test3 = sol.totalFruit(fruits = [1, 2, 3, 2, 2])
    print(test3, 4)
    assert test3 == 4
    