'''
https://leetcode.com/problems/sort-integers-by-the-power-value/description/
'''

class Solution:
    def __init__(self):
        self.power_map = {}

    def get_count(self, num: int) -> int:
        if num == 1:
            return 0

        if num in self.power_map.keys():
            return self.power_map[num]

        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1

        return self.get_count(num) + 1

    def getKth(self, lo: int, hi: int, k: int) -> int:
        results = {}

        for num in range(lo, hi + 1):
            results[num] = self.get_count(num)

        results = list(results.items())
        results.sort(key = lambda x: x[1])

        return results[k - 1][0]
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getKth(lo = 12, hi = 15, k = 2)
    print(test1, 13)
    assert test1 == 13

    test2 = sol.getKth(lo = 7, hi = 11, k = 4)
    print(test2, 7)
    assert test2 == 7
    